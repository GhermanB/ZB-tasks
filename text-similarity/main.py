from fastapi import FastAPI
from pydantic import BaseModel
from text_similarity import SimilarityModel


class Text(BaseModel):
    text1: str
    text2: str


model = SimilarityModel()
app = FastAPI()


@app.post("/similar-recognition")
async def get_body(texts: Text):
    texts_list = list(texts.dict().values())
    return round(model.similarity(texts_list), 4)
