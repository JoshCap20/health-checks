import datetime
import socket
import ssl

from logger import logger


def check_ssl_expiry(url: str, buffer_days: int = 30) -> None:
    hostname = url.split("//")[-1].split("/")[0]
    ctx = ssl.create_default_context()
    try:
        with ctx.wrap_socket(socket.socket(), server_hostname=hostname) as s:
            s.connect((hostname, 443))
            cert = s.getpeercert()
            expiry_date = datetime.datetime.strptime(
                cert["notAfter"], r"%b %d %H:%M:%S %Y %Z"
            )
            if (expiry_date - datetime.datetime.utcnow()).days <= buffer_days:
                logger.warning(
                    f"{url} SSL certificate expiring in less than {buffer_days} days!"
                )
    except Exception as e:
        logger.error(f"Error checking SSL for {url}: {e}")
