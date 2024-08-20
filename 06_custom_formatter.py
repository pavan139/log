import logging

class CustomFormatter(logging.Formatter):
    def format(self, record):
        log_message = super().format(record)
        return f"Custom Format -> {log_message}"

def setup_custom_formatter_logger():
    logger = logging.getLogger("custom_formatter_logger")
    logger.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler()
    custom_formatter = CustomFormatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(custom_formatter)

    logger.addHandler(console_handler)
    return logger

def demonstrate_custom_formatter():
    logger = setup_custom_formatter_logger()
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")

if __name__ == "__main__":
    demonstrate_custom_formatter()
