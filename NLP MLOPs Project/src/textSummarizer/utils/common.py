import os
import yaml
from box.exceptions import BoxValueError
from box import ConfigBox
from pathlib import Path

from src.textSummarizer.logging import logger


def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads yaml file and returns ConfigBox.

    Args:
        path_to_yaml (Path): Path-like input

    Raises:
        ValueError: If yaml file is empty
        e: Empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)

            if content is None:
                raise ValueError("YAML file is empty")

            logger.info(f"yaml file: {path_to_yaml} loaded successfully")

            return ConfigBox(content)

    except BoxValueError:
        raise ValueError("YAML file is empty")

    except Exception as e:
        raise e


def create_directories(path_to_directories: list, verbose=True):
    """
    Create list of directories.

    Args:
        path_to_directories (list): List of paths of directories
        verbose (bool, optional): Print logs. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)

        if verbose:
            logger.info(f"created directory at: {path}")
