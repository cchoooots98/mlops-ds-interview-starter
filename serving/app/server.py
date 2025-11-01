from fastapi import FastAPI
from pydantic import BaseModel
import joblib, os
import numpy as np

MODEL_PATH = os.getenv('MODEL_PATH', 'serving/app/model.pkl')

app = FastAPI(title='Sample Inference API')

class PredictRequest(BaseModel):
    clicks_1h: float
    clicks_24h: float
    purchases_7d: float

@app.get('/health')
def health():
    return {'status':'ok'}

@app.post('/predict')
def predict(req: PredictRequest):
    bundle = joblib.load(MODEL_PATH)
    model = bundle['model']
    X = np.array([[req.clicks_1h, req.clicks_24h, req.purchases_7d]])
    proba = float(model.predict_proba(X)[:,1][0])
    return {'proba': proba}
