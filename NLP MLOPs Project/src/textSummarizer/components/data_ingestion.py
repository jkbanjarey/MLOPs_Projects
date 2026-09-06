from urllib.request import urlretrieve
from zipfile import ZipFile

from src.textSummarizer.entity.config_entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig) -> None:
        self.config = config

    def download_file(self) -> None:
        if self.config.local_data_file.exists():
            return

        self.config.local_data_file.parent.mkdir(parents=True, exist_ok=True)
        urlretrieve(self.config.source_URL, self.config.local_data_file)

    def extract_zip_file(self) -> None:
        self.config.unzip_dir.mkdir(parents=True, exist_ok=True)
        with ZipFile(self.config.local_data_file, "r") as zip_file:
            zip_file.extractall(self.config.unzip_dir)
