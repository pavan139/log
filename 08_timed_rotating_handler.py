import logging
from logging.handlers import TimedRotatingFileHandler

def setup_timed_rotating_logger():
    logger = logging.getLogger("timed_rotating_logger")
    logger.setLevel(logging.DEBUG)

    timed_rotating_handler = TimedRotatingFileHandler(
        "timed_rotating_log.log",
        when="midnight",
        interval=1,
        backupCount=7  # Keep 7 backups
    )
    timed_rotating_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

    logger.addHandler(timed_rotating_handler)
    return logger

def demonstrate_timed_rotating_logger():
    logger = setup_timed_rotating_logger()
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")

if __name__ == "__main__":
    demonstrate_timed_rotating_logger()
