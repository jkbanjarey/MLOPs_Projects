# Student Performance Azure Deployment

This project is a containerized Flask machine learning application for predicting student performance. It includes a regression training pipeline, saved prediction artifacts, Docker support, and a GitHub Actions workflow that builds and deploys the container to Azure Web App.

## Project Structure

- `app.py` - Flask application entry point.
- `src/components/` - data ingestion, transformation, and model training modules.
- `src/pipeline/predict_pipeline.py` - prediction pipeline and input data wrapper.
- `templates/` - web pages for input and results.
- `notebook/` - EDA and model training notebooks.
- `artifacts/` - generated data splits, trained model, and preprocessor.
- `Dockerfile` - container image definition.
- `.github/workflows/main_studentperformancecheck.yml` - Azure container deployment workflow.

## Features

- Predicts math score from form inputs.
- Uses saved model and preprocessing artifacts.
- Supports local Flask execution.
- Supports Docker container execution.
- Deploys to Azure Web App through GitHub Actions.

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Because `requirements.txt` includes `-e .`, the local package is installed in editable mode.

## Run the Application

```bash
python app.py
```

The app runs on:

```text
http://localhost:80
```

On Windows or non-admin shells, binding to port `80` may require elevated permissions. If needed, change the port in `app.py` to `5000` for local development.

## Docker

```bash
docker build -t student-performance-azure .
docker run -p 80:80 student-performance-azure
```

## Training Workflow

Training modules are available under `src/components/`:

1. `data_ingestion.py` loads the dataset and creates train/test splits.
2. `data_transformation.py` builds preprocessing artifacts.
3. `model_trainer.py` trains and evaluates regression models.

The notebooks in `notebook/` show EDA and model experimentation.

## Deployment

The GitHub Actions workflow builds a Docker image, pushes it to Azure Container Registry, and deploys it to Azure Web App.

Required repository secrets include:



## Notes

- The prediction app depends on `artifacts/model.pkl` and `artifacts/preprocessor.pkl`.
- The current form mapping in `app.py` assigns `writing_score` to `reading_score` and `reading_score` to `writing_score`; verify this before production use.
- The workflow image tag path contains `tudentperformance1`; confirm the repository name in Azure Container Registry before deploying.
