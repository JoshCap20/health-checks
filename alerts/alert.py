import json
import logging

from alerts.email_handler import send_email_alert
from alerts.telegram_handler import send_telegram_alert


class AlertHandler(logging.Handler):
    def __init__(self, alert_level, send_alert_fn, *args, **kwargs):
        super().__init__(level=alert_level)
        self.send_alert_fn = send_alert_fn
        self.args = args
        self.kwargs = kwargs

    def emit(self, record):
        self.send_alert_fn(*self.args, message=self.format(record), **self.kwargs)

class EmailAlertManager:
    def __init__(self, logger, config):
        handler = AlertHandler(
            getattr(logging, config["alert_level"]),
            send_email_alert,
            subject="Application Alert",
            to_email=config["to_email"],
            smtp_server=config["smtp_server"],
            smtp_port=config["smtp_port"],
            smtp_user=config["smtp_user"],
            smtp_pass=config["smtp_pass"],
        )
        formatter = logging.Formatter("[%(asctime)s] %(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)

class TelegramAlertManager:
    def __init__(self, logger, config):
        handler = AlertHandler(
            getattr(logging, config["alert_level"]),
            send_telegram_alert,
            bot_token=config["bot_token"],
            user_id=config["user_id"]
        )
        formatter = logging.Formatter("[%(asctime)s] %(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)


class AlertManager:
    def __init__(self, logger, config_path="config.json"):
        with open(config_path, "r") as file:
            self.config = json.load(file)

        with open("config.json", "r") as file:
            config = json.load(file)

        email_config = config["alerts"].get("email", {})
        telegram_config = config["alerts"].get("telegram", {})

        if email_config.get("active"):
            EmailAlertManager(logger, email_config)
            
        if telegram_config.get("active"):
            TelegramAlertManager(logger, telegram_config)