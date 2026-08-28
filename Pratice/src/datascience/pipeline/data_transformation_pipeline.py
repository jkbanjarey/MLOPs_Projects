import os
from src.datascience.components.data_tranasformation import DataTransformation
from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.data_tranasformation import DataTransformation
from src.datascience import logger

STAGE_NAME = "Data Transformation Stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_transformation(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.train_test_spilitting()


if __name__ == '__main__':
    try:
        logger.info(f"----{STAGE_NAME} started ----")
        pipeline = DataTransformationTrainingPipeline()
        pipeline.initiate_data_transformation()
        logger.info(f"----{STAGE_NAME} completed ----")
    except Exception as e:
        logger.error(f"Error occurred while initiating data transformation: {e}")