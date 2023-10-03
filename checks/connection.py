import socket

from utils.logger import logger


def check_connection() -> bool:
    """Check if the device is connected to the internet."""
    try:
        socket.create_connection(("8.8.8.8", 53))
        logger.info("Connected to Wi-Fi.")
        return True
    except OSError:
        logger.error("Not connected to Wi-Fi.")
    return False
