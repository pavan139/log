import logging

class CustomFilter(logging.Filter):
    def filter(self, record):
        return "specific" in record.getMessage()

def setup_logger_with_filter():
    logger = logging.getLogger("filtered_logger")
    logger.setLevel(logging.DEBUG)

    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    
    # Adding the custom filter
    handler.addFilter(CustomFilter())

    logger.addHandler(handler)
    return logger

def demonstrate_logging_filter():
    logger = setup_logger_with_filter()
    logger.debug("This is a debug message without the specific keyword")
    logger.info("This message contains the specific keyword")

if __name__ == "__main__":
    demonstrate_logging_filter()
