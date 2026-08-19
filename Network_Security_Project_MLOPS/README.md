# Network Security MLOps Project

This project builds a phishing website detection system with a FastAPI service, MongoDB-based data ingestion, a modular training pipeline, model artifacts, Docker support, and AWS ECR/ECS-style deployment automation.

## Project Structure

- `app.py` - FastAPI application with training and batch prediction endpoints.
- `main.py` - local training pipeline runner.
- `networksecurity/components/` - ingestion, validation, transformation, and model training components.
- `networksecurity/pipeline/training_pipeline.py` - end-to-end training orchestration.
- `networksecurity/entity/` - configuration and artifact data classes.
- `networksecurity/utils/` - serialization, model utilities, and helper functions.
- `networksecurity/cloud/s3_syncer.py` - S3 synchronization helper.
- `data_schema/schema.yaml` - expected input schema for phishing data.
- `Network_Data/phisingData.csv` - source phishing dataset.
- `final_model/` - trained model and preprocessor used by prediction.
- `prediction_output/output.csv` - latest generated prediction output.
- `.github/workflows/main.yml` - CI/CD workflow for AWS ECR deployment and self-hosted runner execution.

## Features

- Reads phishing data from MongoDB during training.
- Validates incoming data against the schema in `data_schema/schema.yaml`.
- Performs data transformation and preprocessing.
- Trains a classification model and saves final artifacts.
- Serves a FastAPI API with Swagger documentation.
- Supports CSV upload for prediction.
- Includes Docker and GitHub Actions deployment configuration.

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Create a `.env` file with:

```text
MONGODB_URL_KEY=<your-mongodb-connection-string>
```

AWS credentials are required only when syncing training artifacts and final models to S3.

## Run Locally

Start the API:

```bash
python app.py
```

Open the API docs:

```text
http://localhost:8000/docs
```

Run the training pipeline from the API:

```text
GET /train
```

Run a batch prediction:

```text
POST /predict
```

Upload a CSV file with the columns defined in `data_schema/schema.yaml`.

## Local Training Without API

```bash
python main.py
```

## Docker

```bash
docker build -t network-security-mlops .
docker run -p 8000:8000 --env-file .env network-security-mlops
```

## Deployment

The GitHub Actions workflow:

1. Runs placeholder lint and test steps.
2. Builds and pushes a Docker image to Amazon ECR.
3. Pulls and runs the image on a self-hosted deployment runner.

Required repository secrets include:

- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `AWS_REGION`
- `AWS_ECR_LOGIN_URI`
- `ECR_REPOSITORY_NAME`

## Notes

- The application loads prediction artifacts from `final_model/model.pkl` and `final_model/preprocessor.pkl`.
- The API runs on port `8000`, while the current workflow maps Docker port `8080:8080`; align the Docker/runtime port mapping before deployment.
- Training requires a valid MongoDB connection string and AWS permissions if S3 sync is enabled.
