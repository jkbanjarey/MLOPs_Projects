import os
import yaml
from src.datascience import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
from box.exceptions import BoxValueError

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads a YAML file and returns its contents as a ConfigBox."""
    try:
        with open(path_to_yaml, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)
        return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty.")
    except Exception as e:
        raise ValueError(f"Error occurred while reading YAML file: {e}")

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """Creates directories if they don't exist."""
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Directory created: {path}")

@ensure_annotations
def save_json(path: Path, data: dict):
    """Saves data to a JSON file."""
    with open(path, "w") as json_file:
        json.dump(data, json_file, indent=4)

    logger.info(f"JSON file saved: {path}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """Loads data from a JSON file."""
    with open(path, "r") as json_file:
        data = json.load(json_file)
    logger.info(f"JSON file loaded: {path}")
    return ConfigBox(data)

@ensure_annotations
def save_bin(path: Path, data: Any):
    """Saves data to a binary file."""
    joblib.dump(value=data, filename=path)
    logger.info(f"Binary file saved: {path}")
