from fastapi import FastAPI, File, UploadFile
from OCR_model import OCR_Model

model = OCR_Model()
app = FastAPI()


@app.post("/text-recognition")
async def create_upload_file(file: UploadFile = File(...)):
    content = await file.read()
    detected_text = model.read_image(content)
    return detected_text
