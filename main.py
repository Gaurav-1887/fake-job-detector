from fastapi import FastAPI
from pydantic import BaseModel
import pickle
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

class JobInput(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "API running 🚀"}

@app.post("/predict")
def predict(data: JobInput):
    vec = vectorizer.transform([data.text])
    pred = model.predict(vec)[0]
    prob = model.predict_proba(vec)[0].max()

    return {
        "prediction": int(pred),
        "confidence": float(prob)
    }