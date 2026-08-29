import os
from src.datascience.components.model_trainer import ModelTrainer
from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.model_evaluation import ModelEvaluation
from src.datascience import logger


STAGE_NAME = "Model Evaluation Stage"

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def initiate_model_evaluation(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(config=model_evaluation_config)
        model_evaluation.log_into_mlflow()



if __name__ == '__main__':
    try:
        logger.info(f"----{STAGE_NAME} started ----")
        pipeline = ModelEvaluationPipeline()
        pipeline.initiate_model_evaluation()
        logger.info(f"----{STAGE_NAME} completed ----")
    except Exception as e:
        logger.error(f"Error occurred while initiating model evaluation: {e}")