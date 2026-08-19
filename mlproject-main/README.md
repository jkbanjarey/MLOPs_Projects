# Student Performance Prediction

This project is an end-to-end machine learning web application for predicting a student's math score from demographic and academic inputs. It includes exploratory notebooks, a training pipeline, saved model artifacts, a Flask prediction app, and an Azure App Service deployment workflow.

## Project Structure

- `app.py` - Flask application entry point.
- `src/components/` - data ingestion, transformation, and model training modules.
- `src/pipeline/predict_pipeline.py` - prediction pipeline and request data formatting.
- `src/utils.py` - model persistence, loading, and model evaluation helpers.
- `templates/` - Flask HTML templates.
- `notebook/` - EDA and model training notebooks.
- `artifacts/` - generated data splits, trained model, and preprocessor.
- `.github/workflows/main_studentssperformance3.yml` - GitHub Actions workflow for Azure deployment.
- `.ebextensions/` - Elastic Beanstalk Python configuration.

## Features

- Trains and compares multiple regression models.
- Uses preprocessing artifacts for consistent inference.
- Serves predictions through a Flask form.
- Includes pre-generated `model.pkl` and `preprocessor.pkl` files in `artifacts/`.
- Includes CI/CD configuration for Azure Web App deployment.

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

To install the project as an editable package, uncomment `-e .` in `requirements.txt` or run:

```bash
pip install -e .
```

## Run the Application

```bash
python app.py
```

The app starts on `0.0.0.0` using Flask's default port `5000`.

Open:

```text
http://localhost:5000/predictdata
```

## Training Workflow

The training code is organized under `src/components/`:

1. `data_ingestion.py` loads the source data and creates train/test splits.
2. `data_transformation.py` builds preprocessing artifacts.
3. `model_trainer.py` trains and evaluates regression models.

The notebooks in `notebook/` document EDA and model experimentation.

## Deployment

The GitHub Actions workflow builds the Python application and deploys it to Azure App Service using a publish profile secret.

Required repository secret:

-

## Notes

- The prediction app depends on `artifacts/model.pkl` and `artifacts/preprocessor.pkl`.
- `src/pipeline/predict_pipeline.py` uses `os.path` and should import `os` before running in a clean environment.
- The current form mapping in `app.py` assigns `writing_score` to `reading_score` and `reading_score` to `writing_score`; verify this before production use.
