from make_answer import singleton
from queue import Queue

from make_answer.chat.llm_worker import LlmWorkers


@singleton
class LlmApiWorkers(LlmWorkers):
    def __init__(self):
        super().__init__()

    def init(
        self, worker_class, worker_num: int = 1,
        *worker_args, **worker_kwargs
    ):
        if self._is_init:
            return
        self._workers = Queue(worker_num)
        for i in range(worker_num):
            self._workers.put(worker_class(*worker_args, **worker_kwargs))
        self._is_init = True
        self._sleep_time = 0
        if "sleep_time" in worker_kwargs:
            self._sleep_time = worker_kwargs["sleep_time"]

