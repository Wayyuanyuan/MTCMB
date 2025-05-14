import random
from queue import Queue
import itertools

from make_answer import singleton
from make_answer.chat.llm_worker import LlmWorkers


@singleton
class LlmLocalWorkers(LlmWorkers):
    def __init__(self):
        super().__init__()

    # 一张显卡太慢了，思考怎么多进程调用
    def init(
        self, model_path: str, cls,
        worker_num: int = 1, num_gpus: str = "0", sleep_time: float = 0
    ):
        if self._is_init:
            return
        num_gpus = list(map(int, num_gpus.split(",")))
        self._workers = Queue(worker_num)
        gpu_cycle = itertools.cycle(num_gpus)
        for i in range(worker_num):
            self._workers.put(cls(model_path, next(gpu_cycle)))
        self._is_init = True
        self.sleep_time = sleep_time
