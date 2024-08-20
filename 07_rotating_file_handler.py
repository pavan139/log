import logging
from logging.handlers import RotatingFileHandler

def setup_rotating_file_logger():
    logger = logging.getLogger("rotating_logger")
    logger.setLevel(logging.DEBUG)

    rotating_handler = RotatingFileHandler(
        "rotating_log.log",
        maxBytes=500,  # Rotate log after 500 bytes
        backupCount=3  # Keep 3 backups
    )
    rotating_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

    logger.addHandler(rotating_handler)
    return logger

def demonstrate_rotating_logger():
    logger = setup_rotating_file_logger()
    for i in range(20):
        logger.debug(f"Debug message {i}")

if __name__ == "__main__":
    demonstrate_rotating_logger()
