from fastapi import FastAPI
from backend.services.gemini_service import get_gemini_response
from backend.models.chat_model import ChatRequest
app = FastAPI(
    title="KindMind AI API",
    description="Backend API for KindMind AI",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to KindMind AI Backend!"
    }

@app.post("/chat")
def chat(request: ChatRequest):
    response = get_gemini_response(request.message)

    return {
        "response": response
    }