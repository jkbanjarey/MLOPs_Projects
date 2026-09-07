from src.textSummarizer.logging import logger
from src.textSummarizer.pipeline.data_ingestion_pipeline import DataIngestionPipeline

STAGE_NAME = "Data Ingestion"

try:
    logger.info(f"Initiating {STAGE_NAME} stage")
    data_ingestion_pipeline = DataIngestionPipeline()
    data_ingestion_pipeline.initiate_data_ingestion()
    logger.info(f"Completed {STAGE_NAME} stage")
except Exception as e:
    logger.error(f"Error occurred in {STAGE_NAME} stage: {e}")