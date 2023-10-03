
import time
import requests
import logging
import sys

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create console handler and set level to INFO
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)

# Create formatter
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# Add formatter to handler
handler.setFormatter(formatter)

# Add handler to logger
logger.addHandler(handler)


class HealthChecker:
    TEST_ENDPOINTS: list[dict] = [
        {'django-backend': [
            "https://scanbandz.com",
            "https://scanbandz.com/host",
        ]},
        {'angular-ticket-frontend': [
            "https://tickets.scanbandz.com",
            "https://tickets.scanbandz.com/event/32",
        ]}
    ]

    def run(self) -> None:
        print("\n\n")
        logger.info("Starting health check at " +
                    time.strftime("%H:%M:%S", time.localtime()))
        for endpoint in self.TEST_ENDPOINTS:
            for key, value in endpoint.items():
                logger.info('\033[34m' + f"Checking {key}..." + '\033[0m')
                for url in value:
                    if self.ping_page(url):
                        logger.info(
                            '\033[32m' + f"Endpoint {url} is up!" + '\033[0m')
                    else:
                        self.handle_issue(url)
                logger.info('\033[34m' + f"Finished checking {key}." + '\033[0m')
        logger.info("Finished health check at " +
                    time.strftime("%H:%M:%S", time.localtime()))

    def ping_page(self, url: str) -> bool:
        try:
            response = requests.get(url)
            return response.status_code == 200
        except:
            return False

    def handle_issue(self, url: str) -> None:
        logger.error('\033[31m' + f"Endpoint {url} is down!" + '\033[0m')
        with open("errors.txt", "a") as f:
            f.write(f"Endpoint {url} is down!\n")


if __name__ == "__main__":
    while True:
        HealthChecker().run()
        time.sleep(60)
