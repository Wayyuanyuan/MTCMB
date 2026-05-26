import os
import time

import openai
from loguru import logger

from make_answer.chat.chat_invoker import ChatInvoker

OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"

OPENROUTER_GEMINI_DEFAULT = "google/gemini-2.5-flash"

OPENROUTER_MODEL_ALIASES: dict[str, str] = {
    "gemini": OPENROUTER_GEMINI_DEFAULT,
    "gemini-1.5-pro": OPENROUTER_GEMINI_DEFAULT,
    "gemini-2.0-flash": "google/gemini-2.0-flash-001",
    "gemini-2.5-flash": "google/gemini-2.5-flash",
    "gemini-2.5-pro": "google/gemini-2.5-pro",
    "gemini-3-flash": "google/gemini-3-flash-preview",
    "deepseek-chat": "deepseek/deepseek-chat",
}


def resolve_openrouter_model(name: str) -> str:
    key = name.strip()
    return OPENROUTER_MODEL_ALIASES.get(key, key)


def _retryable_status(exc: Exception) -> bool:
    if isinstance(exc, openai.APIStatusError):
        return exc.status_code in (429, 500, 502, 503, 504)
    return False


class LlmOpenRouter(ChatInvoker):
    """OpenRouter（OpenAI 兼容接口）。"""

    def __init__(self, *args, **kwargs):
        api_key = kwargs.get("api_key") or os.environ.get("OPENROUTER_API_KEY")
        if not api_key:
            raise ValueError("请设置 OPENROUTER_API_KEY 或传入 --api-key")

        # API 模型以 OPENROUTER_MODEL 为准；--llm-name 仅用于输出目录名
        raw_model = (
            os.environ.get("OPENROUTER_MODEL", "").strip()
            or str(kwargs.get("model_name") or "").strip()
            or OPENROUTER_GEMINI_DEFAULT
        )
        self.model_name = resolve_openrouter_model(raw_model)

        referer = kwargs.get("http_referer") or os.environ.get(
            "OPENROUTER_HTTP_REFERER", "https://github.com/MTCMB"
        )
        title = kwargs.get("site_title") or os.environ.get(
            "OPENROUTER_SITE_TITLE", "MTCMB"
        )

        self.client = openai.OpenAI(
            base_url=OPENROUTER_BASE_URL,
            api_key=api_key,
            default_headers={
                "HTTP-Referer": referer,
                "X-OpenRouter-Title": title,
            },
        )
        default_max = "2560" if "pro" in self.model_name.lower() else "4096"
        self.max_tokens = int(os.environ.get("OPENROUTER_MAX_TOKENS", default_max))
        self.max_retries = int(os.environ.get("OPENROUTER_MAX_RETRIES", "3"))
        self.retry_sleep = float(os.environ.get("OPENROUTER_RETRY_SLEEP", "3"))

    def _create_completion(self, msg: str):
        return self.client.chat.completions.create(
            model=self.model_name,
            max_tokens=self.max_tokens,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "你是精通中医基础理论、中医教育测评的专家。"
                        "按用户要求的中文要点格式作答，表述须准确、规范。"
                    ),
                },
                {"role": "user", "content": msg},
            ],
        )

    def _content_from_response(self, response) -> str:
        if not response.choices:
            raise ValueError(f"OpenRouter 无 choices (model={self.model_name})")
        choice = response.choices[0]
        content = choice.message.content
        if content is None or not str(content).strip():
            raise ValueError(
                f"OpenRouter 返回 content 为空 "
                f"(model={self.model_name}, finish_reason={choice.finish_reason})"
            )
        return str(content)

    def chat(self, msg: str, *args, **kwargs) -> str:
        last_err: Exception | None = None
        for attempt in range(1, self.max_retries + 1):
            try:
                response = self._create_completion(msg)
                return self._content_from_response(response)
            except openai.APIStatusError as e:
                last_err = e
                if e.status_code == 402:
                    raise ValueError(
                        f"OpenRouter 额度不足 (402)：请降低 OPENROUTER_MAX_TOKENS "
                        f"(当前 {self.max_tokens}) 或充值。原始信息: {e.message}"
                    ) from e
                if _retryable_status(e) and attempt < self.max_retries:
                    logger.warning(
                        f"OpenRouter {e.status_code}，{self.retry_sleep}s 后重试 "
                        f"({attempt}/{self.max_retries})"
                    )
                    time.sleep(self.retry_sleep)
                    continue
                logger.exception("call OpenRouter chat api error")
                raise
            except ValueError as e:
                last_err = e
                if "content 为空" in str(e) and attempt < self.max_retries:
                    logger.warning(
                        f"{e}，{self.retry_sleep}s 后重试 ({attempt}/{self.max_retries})"
                    )
                    time.sleep(self.retry_sleep)
                    continue
                raise
            except Exception as e:
                last_err = e
                logger.exception("call OpenRouter chat api error")
                raise

        raise last_err or RuntimeError("OpenRouter 重试耗尽")
