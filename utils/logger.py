import logging
import sys

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)  # This will allow the logger to process all messages.

# Formatter
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

# Console handler
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)

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

# Add the handlers to the logger
logger.addHandler(console_handler)
logger.addHandler(info_file_handler)
logger.addHandler(debug_file_handler)
logger.addHandler(error_file_handler)
