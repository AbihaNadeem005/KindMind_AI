def detect_emotion(user_message: str) -> str:
    """
    Detects the user's emotion using simple keyword matching.
    """

    message = user_message.lower()

    # Happy
    if any(word in message for word in [
        "happy", "glad", "joy", "wonderful", "great",
        "awesome", "smile"
    ]):
        return "Happy"

    # Excited
    elif any(word in message for word in [
        "excited", "amazing", "finally", "yay",
        "can't wait", "thrilled", "project is working"
    ]):
        return "Excited"

    # Sad
    elif any(word in message for word in [
        "sad", "cry", "depressed", "failed",
        "upset", "heartbroken", "unhappy"
    ]):
        return "Sad"

    # Angry
    elif any(word in message for word in [
        "angry", "mad", "furious",
        "annoyed", "hate"
    ]):
        return "Angry"

    # Anxious
    elif any(word in message for word in [
        "anxious", "nervous", "interview",
        "presentation", "worried", "panic"
    ]):
        return "Anxious"

    # Stressed
    elif any(word in message for word in [
        "stressed", "stress", "pressure",
        "overwhelmed", "busy", "deadline"
    ]):
        return "Stressed"

    return "Neutral"