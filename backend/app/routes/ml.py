
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import joblib, os, numpy as np

router = APIRouter()

MODEL_PATH = os.path.join(os.path.dirname(__file__), '..', '..', 'ai-analytics', 'models', 'simple_model.joblib')
if not os.path.exists(MODEL_PATH):
    # try alternative path
    MODEL_PATH = os.path.join(os.path.dirname(__file__), '..', '..', 'ai-analytics', 'simple_model.joblib')

class PredictIn(BaseModel):
    features: list

class PredictOut(BaseModel):
    prediction: int

@router.post('/predict', response_model=PredictOut)
async def predict(payload: PredictIn):
    if not os.path.exists(MODEL_PATH):
        raise HTTPException(500, 'Model not found. Train model first.')
    model = joblib.load(MODEL_PATH)
    x = np.array(payload.features).reshape(1, -1)
    pred = int(model.predict(x)[0])
    return {'prediction': pred}
