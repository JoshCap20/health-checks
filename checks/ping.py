import time

import requests

from utils.logger import logger


def check_ping(
    url: str, error_response_time: float, warning_response_time: float, retries: int = 3
) -> None:
    for _ in range(retries):
        try:
            start_time = time.time()
            response = requests.get(url)
            response_time = time.time() - start_time
            if response.status_code == 200:
                if response_time > error_response_time:
                    logger.error(
                        f"Endpoint {url} is up but slow with a response time of {response_time:.2f} seconds!"
                    )
                elif response_time > warning_response_time:
                    logger.warning(
                        f"Endpoint {url} is up but slow with a response time of {response_time:.2f} seconds!"
                    )
                else:
                    logger.info(
                        f"Endpoint {url} is up with a response time of {response_time:.2f} seconds!"
                    )
                return
        except requests.RequestException:
            logger.debug(f"Endpoint {url} failed to respond on attempt {_ + 1}.")
    logger.error(f"Endpoint {url} returned a {response.status_code}")
