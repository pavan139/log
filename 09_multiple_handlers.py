import logging

def setup_logger_with_multiple_handlers():
    logger = logging.getLogger("multi_handler_logger")
    logger.setLevel(logging.DEBUG)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    console_handler.setLevel(logging.INFO)

    # File handler
    file_handler = logging.FileHandler("multi_handler.log")
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    file_handler.setLevel(logging.DEBUG)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    
    return logger

def demonstrate_multiple_handlers():
    logger = setup_logger_with_multiple_handlers()
    logger.debug("This debug message goes to file only")
    logger.info("This info message goes to both console and file")
    logger.warning("This warning message goes to both console and file")
    logger.error("This error message goes to both console and file")
    logger.critical("This critical message goes to both console and file")

if __name__ == "__main__":
    demonstrate_multiple_handlers()
