from src.datascience import logger
from src.datascience.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline


STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f"----{STAGE_NAME} started ----")
    pipeline = DataIngestionTrainingPipeline()
    pipeline.initiate_data_ingestion()
    logger.info(f"----{STAGE_NAME} completed ----")
except Exception as e:
    logger.error(f"Error occurred while initiating data ingestion: {e}")
    