from fastapi import FastAPI
from pydantic import BaseModel
from core.model import query_model

app = FastAPI()

class Prompt(BaseModel):
    message: str

@app.get("/")
def home():
    return {"status": "AscendenceAgent running"}

@app.post("/chat")
def chat(prompt: Prompt):
    return {"response": query_model(prompt.message)}