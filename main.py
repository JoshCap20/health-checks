import argparse
import sys
import time

import checks.connection as conn_check
import checks.ping as ping_check
import checks.ssl_expiry as ssl_check
from health_checker import HealthChecker
from logger import logger


def get_args():
    parser = argparse.ArgumentParser(description="Health Checker Tool")

    # Ping timeout argument
    parser.add_argument(
        "--ping-timeout",
        type=int,
        default=180,
        help="Ping timeout in seconds. Default is 180 seconds.",
    )

    # URLs argument (comma-separated)
    parser.add_argument(
        "--urls",
        type=str,
        required=True,
        help="Comma-separated list of URLs to be checked.",
    )

    # Modules argument (comma-separated)
    parser.add_argument(
        "--modules",
        type=str,
        default="ping",
        help="Comma-separated list of modules to be used for checking. Available modules: ping, ssl_expiry. Default is 'ping,ssl_expiry'.",
    )

    # Min response time argument
    parser.add_argument(
        "--error-response-time",
        type=float,
        default=2,  # 2000ms as an example default
        help="Minimum acceptable response time in seconds. Any response slower than this will trigger an error.",
    )

    # Warning response time argument
    parser.add_argument(
        "--warning-response-time",
        type=float,
        default=1,  # 1000ms as an example default
        help="Response time in seconds to trigger a warning. Any response slower than this will trigger a warning or error, but faster than min-response-time will not trigger an error.",
    )

    return parser.parse_args()


if __name__ == "__main__":
    args = get_args()
    urls = args.urls.split(",")
    modules = args.modules.split(",")

    while True:
        if conn_check.check_connection():
            functions = []
            for module in modules:
                if module == "ping":
                    functions.append(lambda url: ping_check.check_ping(url=url, error_response_time=args.error_response_time, warning_response_time=args.warning_response_time))
            HealthChecker.run(urls, functions)
        else:
            logger.error("Lost Wi-Fi connectivity. Stopping health checks.")
            should_resume: str = input("Would you like to resume health checks? (y/n) ")
            if should_resume.lower() == "y":
                logger.info("Resuming health checks.")
            else:
                logger.info("Exiting.")
                sys.exit()
        time.sleep(args.ping_timeout)
