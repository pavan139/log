import logging

# Logging to a File
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("application.log"),  # Logs to a file
        logging.StreamHandler()  # Also logs to console
    ]
)

def demonstrate_logging_to_file():
    logging.debug("This is a debug message")
    logging.info("This is an info message")
    logging.warning("This is a warning message")
    logging.error("This is an error message")
    logging.critical("This is a critical message")

if __name__ == "__main__":
    demonstrate_logging_to_file()
