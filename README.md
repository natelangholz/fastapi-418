# fastapi-418

A lightweight machine learning API project built with:

- Jupyter notebooks for exploration and model training
- FastAPI for serving predictions

## Project Structure

```text
fastapi-418/
├── app/
│   └── main.py
├── models/
├── notebooks/
│   └── iris_modeling.ipynb
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── pyproject.toml
└── README.md
```

## Setup

Using `uv`:

```bash
cd fastapi-418
uv venv
source .venv/bin/activate
uv pip install -e .
```

Or with pip:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

## Notebook Workflow

Launch Jupyter:

```bash
jupyter notebook
```

Then open:

```text
notebooks/iris_modeling.ipynb
```

The notebook workflow:
- load the iris dataset
- create a scatter plot
- calculate correlation
- fit two linear models
- save the final model to `models/model_2.pkl`

Run the final save-model cell before starting the API.

## Run the API Locally

```bash
python -m app.main
```

## API Endpoints

Health check:

```bash
curl -X GET "http://localhost:8080/health_check"
```

Prediction:

```bash
curl -X POST "http://localhost:8080/predict_petal_length" \
  -H "Content-Type: application/json" \
  -d '{"petal_width": 5, "sepal_length": 5}'
```

## Run with Podman

Build the image:

```bash
podman build -t fastapi-418:latest .
```

Run the container:

```bash
podman run --rm -p 8080:8080 fastapi-418:latest
```

Use compose:

```bash
podman compose up --build
```

## Notes

- The API expects `models/model_2.pkl` to exist before prediction requests are made.
- Because the model is created by the notebook, generate `models/model_2.pkl` before building the container image.