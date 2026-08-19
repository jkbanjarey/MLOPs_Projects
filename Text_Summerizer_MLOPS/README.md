# Text Summarizer MLOps

This project trains and serves a dialogue summarization model using Hugging Face Transformers. It follows a staged MLOps-style pipeline for data ingestion, transformation, model training, evaluation, and FastAPI inference.

## Project Structure

- `app.py` - FastAPI application with training and prediction endpoints.
- `main.py` - full training pipeline runner.
- `config/config.yaml` - artifact paths, dataset URL, tokenizer, and model checkpoint configuration.
- `params.yaml` - training hyperparameters.
- `src/textSummarizer/components/` - pipeline stage implementations.
- `src/textSummarizer/pipeline/` - stage orchestration and prediction pipeline.
- `src/textSummarizer/config/configuration.py` - configuration manager.
- `src/textSummarizer/entity/` - configuration data classes.
- `research/` - notebooks for experimentation and staged development.
- `template.py` - scaffold script used to create the project structure.

## Pipeline

The training flow in `main.py` runs these stages:

1. Data ingestion downloads and extracts the SAMSum dataset.
2. Data transformation tokenizes and prepares the dataset.
3. Model training fine-tunes `google/pegasus-cnn_dailymail`.
4. Model evaluation calculates ROUGE metrics and writes them to `artifacts/model_evaluation/metrics.csv`.

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

The project uses PyTorch and Transformers. Training is much faster with a CUDA-capable GPU, but the code can fall back to CPU.

## Train the Model

```bash
python main.py
```

Artifacts are written under the `artifacts/` directory configured in `config/config.yaml`.

## Run the API

```bash
python app.py
```

Open:

```text
http://localhost:8080/docs
```

Available endpoints:

- `GET /train` - runs `main.py` and starts the full training pipeline.
- `POST /predict` - summarizes input text using the trained model and tokenizer.

## Prediction Artifacts

The prediction pipeline expects:

- `artifacts/model_trainer/pegasus-samsum-model`
- `artifacts/model_trainer/tokenizer`

Generate these by running the training pipeline before calling `/predict`.

## Configuration

Update `config/config.yaml` to change:

- dataset source URL
- artifact directories
- tokenizer name
- model checkpoint
- evaluation output path

Update `params.yaml` to tune training arguments such as epochs, batch size, warmup steps, and gradient accumulation.

## Notes

- `Dockerfile` and `setup.py` are currently empty placeholders.
- The prediction pipeline file is named `predicition_pipeline.py`; keep imports aligned if renaming it.
- The default dataset URL points to a remote ZIP file, so data ingestion requires internet access.
