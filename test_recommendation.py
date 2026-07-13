from backend.services.recommendation_service import get_recommendation

emotion = "Sad"

recommendation = get_recommendation(emotion)

print("Emotion:", emotion)
print("Recommendation:", recommendation)