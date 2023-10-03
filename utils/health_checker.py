import time
from typing import Callable, List

from .logger import logger


class HealthChecker:
    @staticmethod
    def run(checks: dict[Callable : list[str]]) -> None:
        logger.info(
            "Starting health check at %s", time.strftime("%H:%M:%S", time.localtime())
        )
        for check, args in checks.items():
            for arg in args:
                check(arg)
        logger.info(
            "Finished health check at %s", time.strftime("%H:%M:%S", time.localtime())
        )
