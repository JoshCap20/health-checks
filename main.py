import sys
import time

from logger import logger
import checks.ping as ping_check
import checks.ssl_expiry as ssl_check
import checks.connection as conn_check
import checks.config as config_check

from config import PING_TIMEOUT, TEST_URLS

class HealthChecker:
    @staticmethod
    def run() -> None:
        logger.info("Starting health check at %s", time.strftime("%H:%M:%S", time.localtime()))
        
        # Validate the config first
        if not config_check.validate_config(TEST_URLS):
            logger.error("Configuration validation failed!")
            sys.exit(1)

        for key, value in TEST_URLS.items():
            logger.info("Checking %s...", key)
            for url in value:
                ping_check.check_ping(url)
                ssl_check.check_ssl_expiry(url)
            logger.info("Finished checking %s.", key)
            
        logger.info("Finished health check at %s", time.strftime("%H:%M:%S", time.localtime()))


if __name__ == "__main__":
    while True:
        if conn_check.check_connection():
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
