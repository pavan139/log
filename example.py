import logging
from logging.handlers import RotatingFileHandler
import pandas as pd

def setup_logger():
    logger = logging.getLogger("ETL_Pipeline")
    logger.setLevel(logging.DEBUG)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(console_formatter)

    # File handler with rotation
    file_handler = RotatingFileHandler("etl_pipeline.log", maxBytes=1000000, backupCount=3)
    file_handler.setLevel(logging.DEBUG)
    file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(file_formatter)

    # Adding handlers to logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger

logger = setup_logger()

def extract_data(file_path):
    logger.info(f"Starting data extraction from {file_path}")
    try:
        data = pd.read_csv(file_path)
        logger.info(f"Data extraction successful, {len(data)} records extracted")
        return data
    except Exception as e:
        logger.error(f"Error during data extraction: {e}")
        raise  # Re-raise the exception after logging

def transform_data(data):
    logger.info("Starting data transformation")

    try:
        # Example Transformation: Filter and aggregate data
        filtered_data = data[data['column_name'] > 0]  # Simple filter
        aggregated_data = filtered_data.groupby('group_column').sum()  # Aggregation

        logger.info(f"Data transformation successful, {len(aggregated_data)} records after transformation")
        return aggregated_data
    except Exception as e:
        logger.error(f"Error during data transformation: {e}")
        raise

def load_data(data, output_file_path):
    logger.info(f"Starting data load into {output_file_path}")
    
    try:
        data.to_csv(output_file_path, index=False)
        logger.info("Data load successful")
    except Exception as e:
        logger.error(f"Error during data load: {e}")
        raise

def run_etl_pipeline(input_file_path, output_file_path):
    logger.info("ETL pipeline started")
    
    try:
        # Extract
        data = extract_data(input_file_path)
        
        # Transform
        transformed_data = transform_data(data)
        
        # Load
        load_data(transformed_data, output_file_path)
        
        logger.info("ETL pipeline completed successfully")
    except Exception as e:
        logger.critical("ETL pipeline failed")
        logger.critical(e)

if __name__ == "__main__":
    input_file = "input_data.csv"
    output_file = "output_data.csv"
    
    run_etl_pipeline(input_file, output_file)
