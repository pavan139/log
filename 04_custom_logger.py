import logging

def setup_custom_logger():
    # Using __name__ as the logger name so that it matches the module name
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    
    # Adding a console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    logger.addHandler(console_handler)
    
    return logger

def demonstrate_custom_logger():
    logger = setup_custom_logger()
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")

if __name__ == "__main__":
    print(f"The value of __name__ is: {__name__}")
    demonstrate_custom_logger()
