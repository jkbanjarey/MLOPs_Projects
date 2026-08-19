# Machine Learning and MLOps Project Portfolio

This repository is a collection of machine learning, deployment, and MLOps projects. Each project is kept in its own folder with an individual README, source code, notebooks, artifacts, and deployment configuration where applicable.

## Projects Overview

| Project | Description | Main Stack | Deployment / Platform |
| --- | --- | --- | --- |
| [AWS SageMaker Mobile Price Classification](./awssagemaker/) | Trains a Random Forest classifier to predict mobile phone price ranges from tabular features. | Python, scikit-learn, pandas, SageMaker | Amazon SageMaker training workflow |
| [Student Performance Prediction](./mlproject-main/) | End-to-end Flask ML application that predicts student math scores from demographic and academic inputs. | Python, Flask, scikit-learn, pandas | Azure App Service workflow |
| [Network Security MLOps Project](./Network_Security_Project_MLOPS/) | Phishing website detection system with a modular training pipeline, FastAPI service, MongoDB ingestion, Docker, and AWS deployment automation. | Python, FastAPI, MongoDB, scikit-learn, Docker | AWS ECR / self-hosted runner workflow |
| [Student Performance Azure Deployment](./Student_Performance_Azure_deployment/) | Containerized student performance prediction app with Docker and Azure Web App deployment. | Python, Flask, scikit-learn, Docker | Azure Container Registry and Azure Web App |
| [Text Summarizer MLOps](./Text_Summerizer_MLOPS/) | Dialogue summarization project using Hugging Face Transformers and a staged training/evaluation pipeline. | Python, FastAPI, Transformers, PyTorch | Local API; Docker placeholder |

## Repository Structure

```text
.
|-- awssagemaker/
|-- mlproject-main/
|-- Network_Security_Project_MLOPS/
|-- Student_Performance_Azure_deployment/
|-- Text_Summerizer_MLOPS/
`-- README.MD
```

## Common Local Setup

Most projects use a Python virtual environment and a project-specific `requirements.txt` file.

```bash
cd <project-folder>
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Some projects require additional credentials or services:

- MongoDB connection string for the Network Security project.
- AWS credentials for SageMaker, ECR, ECS-style deployment, or S3 sync workflows.
- Azure publish profile, Azure Container Registry, or Azure Web App configuration for Azure deployment projects.
- Internet access and optional GPU acceleration for the Text Summarizer training pipeline.

## Quick Start by Project

### AWS SageMaker Mobile Price Classification

```bash
cd awssagemaker
python script.py --train . --test . --model-dir . --train-file train-V-1.csv --test-file test-V-1.csv
```

### Student Performance Prediction

```bash
cd mlproject-main
python app.py
```

Open:

```text
http://localhost:5000/predictdata
```

### Network Security MLOps Project

```bash
cd Network_Security_Project_MLOPS
python app.py
```

Open:

```text
http://localhost:8000/docs
```

### Student Performance Azure Deployment

```bash
cd Student_Performance_Azure_deployment
python app.py
```

Open:

```text
http://localhost:80
```

If port `80` requires elevated permissions on your machine, use Docker or change the Flask port for local development.

### Text Summarizer MLOps

```bash
cd Text_Summerizer_MLOPS
python main.py
python app.py
```

Open:

```text
http://localhost:8080/docs
```

## Notes

- Each project has its own README with more detailed setup, training, and deployment instructions.
- Some folders include generated artifacts such as trained models, preprocessors, prediction outputs, or dataset splits.
- Review each project's required secrets before running CI/CD workflows.
- Several projects include notebook-based experimentation alongside production-style pipeline code.
