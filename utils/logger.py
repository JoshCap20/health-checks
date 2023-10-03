import logging
import sys

from termcolor import colored

from alerts.alert import AlertManager


class ColoredFormatter(logging.Formatter):
    COLORS = {
        "DEBUG": "blue",
        "INFO": "green",
        "WARNING": "yellow",
        "ERROR": "red",
        "CRITICAL": "magenta",
    }

    def format(self, record):
        log_message = super(ColoredFormatter, self).format(record)
        return colored(log_message, self.COLORS.get(record.levelname))


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

format_string = "[%(asctime)s] %(levelname)s - %(message)s"
date_format = "%d/%b/%Y %H:%M:%S"

# Standard formatter
formatter = logging.Formatter(format_string, datefmt=date_format)

# Colored formatter for console
colored_formatter = ColoredFormatter(format_string, datefmt=date_format)

# Console handler with colored output
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(colored_formatter)

# File handlers
info_file_handler = logging.FileHandler("logs/info.log")
info_file_handler.setLevel(logging.INFO)
info_file_handler.setFormatter(formatter)

debug_file_handler = logging.FileHandler("logs/debug.log")
debug_file_handler.setLevel(logging.DEBUG)
debug_file_handler.setFormatter(formatter)

error_file_handler = logging.FileHandler("logs/error.log")
error_file_handler.setLevel(logging.ERROR)
error_file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(info_file_handler)
logger.addHandler(debug_file_handler)
logger.addHandler(error_file_handler)

# Alert Managers
alert_manager = AlertManager(logger)
