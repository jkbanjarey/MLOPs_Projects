from sklearn.pipeline import Pipeline

from src.datascience import logger
from src.datascience.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.datascience.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline
from src.datascience.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline
from src.datascience.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
from src.datascience.pipeline.model_evaluation_pipeline import ModelEvaluationPipeline
from src.datascience.pipeline.model_trainer_pipeline import ModelTrainerPipeline


STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f"----{STAGE_NAME} started ----")
    pipeline = DataIngestionTrainingPipeline()
    pipeline.initiate_data_ingestion()
    logger.info(f"----{STAGE_NAME} completed ----")
except Exception as e:
    logger.error(f"Error occurred while initiating data ingestion: {e}")


STAGE_NAME = "Data Validation Stage"

try:
    logger.info(f"----{STAGE_NAME} started ----")
    pipeline = DataValidationTrainingPipeline()
    pipeline.initiate_data_validation()
    logger.info(f"----{STAGE_NAME} completed ----")
except Exception as e:
    logger.error(f"Error occurred while initiating data validation: {e}")


STAGE_NAME = "Data Transformation Stage"

try:
    logger.info(f"----{STAGE_NAME} started ----")
    pipeline = DataTransformationTrainingPipeline()
    pipeline.initiate_data_transformation()
    logger.info(f"----{STAGE_NAME} completed ----")
except Exception as e:
    logger.error(f"Error occurred while initiating data transformation: {e}")


STAGE_NAME = "Model Trainer Stage"

try:
    logger.info(f"----{STAGE_NAME} started ----")
    pipeline = ModelTrainerPipeline()
    pipeline.initiate_model_trainer()
    logger.info(f"----{STAGE_NAME} completed ----")
except Exception as e:
    logger.error(f"Error occurred while initiating model trainer: {e}")



STAGE_NAME = "Model Evaluation Stage"

try:
    logger.info(f"----{STAGE_NAME} started ----")
    pipeline = ModelEvaluationPipeline()
    pipeline.initiate_model_evaluation()
    logger.info(f"----{STAGE_NAME} completed ----")
except Exception as e:
    logger.error(f"Error occurred while initiating model evaluation: {e}")