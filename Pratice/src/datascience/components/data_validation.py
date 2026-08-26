import pandas as pd
from src.datascience.entity.config_entity import DataValidationConfig


class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self) -> bool:
        try:
            data = pd.read_csv(self.config.unzip_data_dir, sep=";")
            all_schema = self.config.all_schema.keys()
            validation_status = all(col in all_schema for col in data.columns)

            with open(self.config.STATUS_FILE, "w") as f:
                f.write(f"Validation status: {validation_status}\n")
                for col in data.columns:
                    if col not in all_schema:
                        f.write(f"Column '{col}' is in the data but not in the schema.\n")
                    else:
                        f.write(f"Column '{col}' is in both the data and the schema.\n")
            return validation_status

        except Exception as e:
            print(f"Error occurred while validating columns: {e}")
            return False
