from fastapi import FastAPI
from backend.services.gemini_service import get_gemini_response
from backend.models.chat_model import ChatRequest
from backend.services.emotion_service import detect_emotion
from backend.services.recommendation_service import get_recommendation
from backend.database.database import save_conversation
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

    save_conversation(
    user_message=request.message,
    emotion=emotion,
    recommendation_title=recommendation["title"],
    ai_response=response
    )

    return {
        "emotion": emotion,
        "recommendation": recommendation,
        "response": response
    }