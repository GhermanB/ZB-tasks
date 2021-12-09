from fastapi import FastAPI
from pydantic import BaseModel
from emotion_detection import ED_Model


class Text(BaseModel):
    text: str


model = ED_Model()
app = FastAPI()


@app.post("/emotion-detection")
async def get_body(text: Text):
    text = text.dict()["text"]
    return model.detect_emotion(text)