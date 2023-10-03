import time

import requests

from logger import logger


def ping(url: str, retries: int = 3) -> None:
    for _ in range(retries):
        try:
            start_time = time.time()
            response = requests.get(url)
            response_time = time.time() - start_time
            if response.status_code == 200:
                logger.info(
                    f"Endpoint {url} is up! Response Time: {response_time:.2f}s"
                )
        except requests.RequestException:
            logger.debug(f"Endpoint {url} failed to respond on attempt {_ + 1}.")
    logger.error(f"Endpoint {url} is down!")
