PING_TIMEOUT: int = 180
ERROR_LOG_NAME: str = "logs/error.log"
INFO_LOG_NAME: str = "logs/info.log"

TEST_URLS: dict = {
    "django-backend": [
        "https://scanbandz.com",
        "https://scanbandz.com/host",
    ],
    "angular-ticket-frontend": [
        "https://tickets.scanbandz.com",
        "https://tickets.scanbandz.com/event/32",
        "https://tickets.scanbandz.com/donate/32",
    ],
}
