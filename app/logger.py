import logging
import os


def get_logger() -> logging.Logger:
    logger: logging.Logger = logging.getLogger("recommender_api")

    if not logger.handlers:
        level = os.getenv("LOG_LEVEL", "INFO")
        logger.setLevel(level)

        ch = logging.StreamHandler()
        formatter = logging.Formatter(
            "[%(asctime)s] %(levelname)s in %(module)s: %(message)s"
        )
        ch.setFormatter(formatter)
        logger.addHandler(ch)

    return logger
