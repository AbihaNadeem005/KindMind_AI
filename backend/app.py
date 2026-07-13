from fastapi import FastAPI
from backend.services.gemini_service import get_gemini_response
from backend.models.chat_model import ChatRequest
from backend.services.emotion_service import detect_emotion
from backend.services.recommendation_service import get_recommendation
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

    emotion = detect_emotion(request.message)

    recommendation = get_recommendation(emotion)

    response = get_gemini_response(
        request.message,
        emotion,
        recommendation
    )

    return {
        "emotion": emotion,
        "recommendation": recommendation,
        "response": response
    }