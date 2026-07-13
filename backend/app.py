from fastapi import FastAPI
from backend.services.gemini_service import get_gemini_response
from backend.models.chat_model import ChatRequest
from backend.services.emotion_service import detect_emotion
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

    # Detect emotion
    emotion = detect_emotion(request.message)

    # Generate AI response
    response = get_gemini_response(request.message)

    return {
        "emotion": emotion,
        "response": response
    }