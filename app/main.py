from datetime import datetime, timezone
from pathlib import Path

import joblib
import pandas as pd
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel


class PredictionRequest(BaseModel):
    petal_width: float
    sepal_length: float


app = FastAPI(title="Petal Length API")

MODEL_PATH = Path(__file__).resolve().parent.parent / "models" / "model_2.pkl"
model = joblib.load(MODEL_PATH) if MODEL_PATH.exists() else None


@app.get("/health_check")
def health_check() -> dict[str, str]:
    return {
        "status": "the API is running :) ",
        "time": datetime.now(timezone.utc).isoformat(),
    }


@app.post("/predict_petal_length")
def predict_petal_length(payload: PredictionRequest) -> dict[str, float]:
    if model is None:
        return {"predicted_petal_length": -1.0}

    prediction_data = pd.DataFrame(
        [
            {
                "Petal.Width": payload.petal_width,
                "Sepal.Length": payload.sepal_length,
            }
        ]
    )
    prediction = float(model.predict(prediction_data)[0])
    return {"predicted_petal_length": prediction}


if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8080)

# Made with Bob
