# AWS SageMaker Mobile Price Classification

This project trains a mobile price range classifier with Amazon SageMaker-compatible training code. It uses a Random Forest classifier from scikit-learn, CSV datasets, and a notebook for experimentation.

## Project Structure

- `research.ipynb` - exploratory notebook for data analysis and SageMaker workflow experiments.
- `script.py` - SageMaker training entry point.
- `mob_price_classification_train.csv` - source mobile price classification dataset.
- `train-V-1.csv` - training split used by the SageMaker script.
- `test-V-1.csv` - test split used by the SageMaker script.
- `requirements.txt` - Python dependencies.

## Model

The training script:

1. Reads training and test CSV files from SageMaker input channels.
2. Uses every column except the last as features.
3. Uses the last column as the target label.
4. Trains `RandomForestClassifier`.
5. Saves the model as `model.joblib`.
6. Prints accuracy and classification report metrics for the test data.

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

For notebook work, select the virtual environment as the Jupyter kernel.

## Local Training

The script expects SageMaker-style channel paths. For local execution, provide them explicitly:

```bash
python script.py --train . --test . --model-dir . --train-file train-V-1.csv --test-file test-V-1.csv
```

Optional hyperparameters:

```bash
python script.py --train . --test . --model-dir . --n_estimators 200 --random_state 42
```

## SageMaker Training

Use `script.py` as the estimator entry point. The script reads these environment variables when running inside SageMaker:

- `SM_MODEL_DIR`
- `SM_CHANNEL_TRAIN`
- `SM_CHANNEL_TEST`

The train channel should contain `train-V-1.csv`, and the test channel should contain `test-V-1.csv`.

## Requirements

Core libraries include:

- `sagemaker`
- `scikit-learn`
- `pandas`
- `numpy`
- `ipykernel`
