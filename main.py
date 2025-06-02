from fastapi import FastAPI
from pydantic import BaseModel
from models import predict_category
from utils import mask_pii_entities

app = FastAPI()

class EmailInput(BaseModel):
    input_email_body: str

@app.get("/")
def read_root():
    return {"message": "Email classifier API. Use /docs for Swagger UI or /classify for predictions."}

@app.post("/classify")
def classify_email(input: EmailInput):
    try:
        masked_text = mask_pii_entities(input.input_email_body)
        category = predict_category(masked_text)
        return {
            "category": category,
            "masked_text": masked_text
        }
    except Exception as e:
        return {"error": str(e)}