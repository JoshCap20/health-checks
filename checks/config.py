from logger import logger

def validate_config(config: dict) -> bool:
    if not isinstance(config, dict):
        logger.error("Invalid TEST_URLS configuration. Expected a dictionary.")
        return False
    for key, values in config.items():
        if not isinstance(values, list):
            logger.error(f"Invalid URLs for {key}. Expected a list of URLs.")
            return False
    return True
