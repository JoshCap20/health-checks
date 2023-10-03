import time
from typing import Callable, List

from logger import logger


class HealthChecker:
    @staticmethod
    def run(urls: List[str], funcs: List[Callable]) -> None:
        logger.info(
            "Starting health check at %s", time.strftime("%H:%M:%S", time.localtime())
        )
        for url in urls:
            for func in funcs:
                func(url)
        logger.info(
            "Finished health check at %s", time.strftime("%H:%M:%S", time.localtime())
        )
