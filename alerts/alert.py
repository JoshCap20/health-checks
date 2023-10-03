import json
import logging

from alerts.email_handler import send_email_alert


class AlertHandler(logging.Handler):
    def __init__(self, alert_level, send_alert_fn, *args, **kwargs):
        super().__init__(level=alert_level)
        self.send_alert_fn = send_alert_fn
        self.args = args
        self.kwargs = kwargs

    def emit(self, record):
        self.send_alert_fn(*self.args, message=self.format(record), **self.kwargs)


class AlertFactory:
    @staticmethod
    def create_handler(alert_type, config):
        if alert_type == "email" and config.get("active"):
            return AlertHandler(
                getattr(logging, config["alert_level"]),
                send_email_alert,
                subject="Application Alert",
                to_email=config["to_email"],
                smtp_server=config["smtp_server"],
                smtp_port=config["smtp_port"],
                smtp_user=config["smtp_user"],
                smtp_pass=config["smtp_pass"],
            )
        return None


class AlertManager:
    def __init__(self, logger, config_path="config.json"):
        with open(config_path, "r") as file:
            self.config = json.load(file)

        for alert_type, config in self.config["alerts"].items():
            handler = AlertFactory.create_handler(alert_type, config)
            if handler:
                formatter = logging.Formatter(
                    "[%(asctime)s] %(levelname)s - %(message)s"
                )
                handler.setFormatter(formatter)
                logger.addHandler(handler)
