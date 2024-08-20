import logging

def setup_logger_hierarchy():
    # Parent logger
    parent_logger = logging.getLogger("parent_logger")
    parent_logger.setLevel(logging.DEBUG)
    parent_logger.addHandler(logging.StreamHandler())

    # Child logger inherits settings from the parent
    child_logger = logging.getLogger("parent_logger.child")
    child_logger.setLevel(logging.WARNING)

    return parent_logger, child_logger

def demonstrate_logger_hierarchy():
    parent_logger, child_logger = setup_logger_hierarchy()

    parent_logger.debug("Parent logger debug message")
    parent_logger.warning("Parent logger warning message")

    child_logger.debug("Child logger debug message (won't be shown)")
    child_logger.warning("Child logger warning message")

if __name__ == "__main__":
    demonstrate_logger_hierarchy()
