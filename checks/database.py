import time

import psycopg2  # TODO: Support other databases

from utils.logger import logger


def check_db_connection(
    conn_string: str, error_response_time: float, warning_response_time: float
) -> None:
    try:
        start_time = time.time()

        # Connect to the database
        conn = psycopg2.connect(conn_string)
        cur = conn.cursor()

        # Execute a simple query. For PostgreSQL, this just retrieves the version.
        cur.execute("SELECT version();")
        cur.fetchone()

        response_time = time.time() - start_time

        if response_time > error_response_time:
            logger.error(
                f"Database responded but was slow with a response time of {response_time:.2f} seconds!"
            )
        elif response_time > warning_response_time:
            logger.warning(
                f"Database responded but was a bit slow with a response time of {response_time:.2f} seconds!"
            )
        else:
            logger.info(
                f"Database connected successfully with a response time of {response_time:.2f} seconds!"
            )
    except Exception as e:
        logger.error(f"Failed to connect to database. Error: {e}")
    finally:
        if "cur" in locals():
            cur.close()
        if "conn" in locals():
            conn.close()
