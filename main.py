from fastapi import FastAPI
import joblib
import numpy as np
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

crop_model = joblib.load(r"C:\Users\shubh\krishi_mitra_ai\models\crop_recommendation_model.pkl")
encoder = joblib.load(r"C:\Users\shubh\krishi_mitra_ai\models\crop_label_encoder.pkl")
yield_model = joblib.load(r"C:\Users\shubh\krishi_mitra_ai\models\yield_prediction_model.pkl")


class InputFeatures(BaseModel):
    N: float
    P: float
    K: float
    temperature: float
    humidity: float
    rainfall: float

@app.get("/")
def home():
    return {"message": "Krishi Mitra AI Advisor Running"}

@app.post("/recommend-crop")
def recommend_crop(inp: InputFeatures):
    arr = np.array([[inp.N, inp.P, inp.K, inp.temperature, inp.humidity, inp.rainfall]])
    pred = crop_model.predict(arr)
    crop_name = encoder.inverse_transform(pred)[0]
    return {"recommended_crop": crop_name}

@app.post("/predict-yield")
def predict_yield(inp: InputFeatures):
    arr = np.array([[inp.N, inp.P, inp.K, inp.temperature, inp.humidity, inp.rainfall]])
    pred = yield_model.predict(arr)[0]
    return {"expected_yield": round(float(pred), 2)}
