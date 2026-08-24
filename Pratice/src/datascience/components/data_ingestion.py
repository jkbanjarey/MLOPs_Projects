## components
import os
from flask import request
import requests
from src.datascience.entity.config_entity import DataIngestionConfig
from src.datascience import logger
import zipfile


class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config = config

    # Downloading the zipfile
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            response = requests.get(self.config.source_URL)
            with open(self.config.local_data_file, "wb") as f:
                f.write(response.content)
            logger.info(f"File downloaded successfully: {self.config.local_data_file}")
        else:
            logger.info(f"File already exists: {self.config.local_data_file}")

    def extract_zipfile(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)

        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
