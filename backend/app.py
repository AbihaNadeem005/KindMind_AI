from fastapi import FastAPI
from backend.services.gemini_service import get_gemini_response
from backend.models.chat_model import ChatRequest
from backend.services.emotion_service import detect_emotion
from backend.services.recommendation_service import get_recommendation
from backend.database.database import save_conversation
from backend.services.comfort_plan_service import get_comfort_plan
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

    comfort_plan = get_comfort_plan(emotion)

    response = get_gemini_response(
        request.message,
        emotion,
        recommendation,
        comfort_plan
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
    "comfort_plan": comfort_plan,
    "response": response
    }

