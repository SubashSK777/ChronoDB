from fastapi import FastAPI
from pydantic import BaseModel
from agents.simple_predictor import make_prediction

app = FastAPI()

class UserInput(BaseModel):
    data: str

@app.post("/predict")
def predict(user_input: UserInput):
    prediction = make_prediction(user_input.data)
    return {"prediction": prediction}
