from backend.services.emotion_service import detect_emotion

message = "I failed my exam today and I feel very sad."

emotion = detect_emotion(message)

print("Detected Emotion:", emotion)