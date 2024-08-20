import logging

# Basic Configuration
logging.basicConfig(level=logging.DEBUG)

def demonstrate_basic_logging():
    logging.debug("This is a debug message")
    logging.info("This is an info message")
    logging.warning("This is a warning message")
    logging.error("This is an error message")
    logging.critical("This is a critical message")

if __name__ == "__main__":
    demonstrate_basic_logging()
