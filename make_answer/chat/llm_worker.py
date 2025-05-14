import threading
from queue import Queue

from make_answer.chat.chat_invoker import ChatInvoker


class LlmWorkers(ChatInvoker):
    def __init__(self):
        self._sleep_time: float = 0
        self._workers: Queue[ChatInvoker] = Queue()
        self._lock = threading.Lock()
        self._is_init = False

    def chat(self, msg: str, *args, **kwargs) -> str:
        if not self._is_init:
            raise ValueError("LlmWorkers not init")
        with self._lock:
            worker = self._workers.get()
        try:
            ret = worker.chat(msg, *args, **kwargs)
            if self._sleep_time > 0:
                import time
                time.sleep(self._sleep_time)
        finally:
            with self._lock:
                self._workers.put(worker)

        return ret