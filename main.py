import logging
import socket
import sys
import time

import requests

from config import ERROR_LOG_NAME, INFO_LOG_NAME, PING_TIMEOUT, TEST_URLS

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Formatter
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

# Console handler
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
handler.setFormatter(formatter)
logger.addHandler(handler)

# Log handler
file_handler = logging.FileHandler(INFO_LOG_NAME)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# Error handler
file_handler = logging.FileHandler(ERROR_LOG_NAME)
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


class HealthChecker:
    @staticmethod
    def run() -> None:
        logger.info(
            "Starting health check at %s", time.strftime("%H:%M:%S", time.localtime())
        )
        for key, value in TEST_URLS.items():
            logger.info("Checking %s...", key)
            for url in value:
                if HealthChecker.ping(url):
                    logger.info("Endpoint %s is up!", url)
                else:
                    logger.error("Endpoint %s is down!", url)
            logger.info("Finished checking %s.", key)
        logger.info(
            "Finished health check at %s", time.strftime("%H:%M:%S", time.localtime())
        )

    @staticmethod
    def ping(url: str) -> bool:
        try:
            response = requests.get(url)
            return response.status_code == 200
        except requests.RequestException:
            return False

    @staticmethod
    def is_connected() -> bool:
        """Check if the device is connected to the internet."""
        try:
            socket.create_connection(("8.8.8.8", 53))
            logger.info("Connected to Wi-Fi.")
            return True
        except OSError:
            logger.error("Not connected to Wi-Fi.")
        return False


if __name__ == "__main__":
    while True:
        if HealthChecker.is_connected():
            HealthChecker.run()
        else:
            logger.error("Lost Wi-Fi connectivity. Stopping health checks.")
            should_resume: str = input("Would you like to resume health checks? (y/n) ")
            if should_resume.lower() == "y":
                logger.info("Resuming health checks.")
            else:
                logger.info("Exiting.")
                sys.exit()
        time.sleep(PING_TIMEOUT)
