import logging

from app.config import LOG_LEVEL


def get_logger(name: str):

    if not logging.getLogger().hasHandlers():

        logging.basicConfig(
            level=LOG_LEVEL,
            format=(
                "%(asctime)s | "
                "%(levelname)s | "
                "%(name)s | "
                "%(message)s"
            )
        )

    return logging.getLogger(name)
