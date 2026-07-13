def get_recommendation(emotion: str) -> dict:
    """
    Returns a structured wellness recommendation
    based on the detected emotion.
    """

    recommendations = {
        "Happy": {
            "title": "Gratitude Journal",
            "category": "Reflection",
            "description": "Write down three things you are grateful for today."
        },

        "Sad": {
            "title": "Breathing Exercise",
            "category": "Relaxation",
            "description": "Take five slow deep breaths to help calm your mind."
        },

        "Angry": {
            "title": "Muscle Relaxation",
            "category": "Relaxation",
            "description": "Practice progressive muscle relaxation for five minutes."
        },

        "Anxious": {
            "title": "Mindfulness Meditation",
            "category": "Meditation",
            "description": "Spend five minutes focusing on your breathing."
        },

        "Stressed": {
            "title": "Nature Sounds",
            "category": "Music",
            "description": "Listen to calming nature sounds and relax."
        },

        "Neutral": {
            "title": "Short Walk",
            "category": "Activity",
            "description": "Take a short walk and enjoy some fresh air."
        },

        "Excited": {
            "title": "Achievement Journal",
            "category": "Reflection",
            "description": "Write about today's achievements and celebrate your progress."
        }
    }

    return recommendations.get(
        emotion,
        {
            "title": "Deep Breathing",
            "category": "Relaxation",
            "description": "Take a few deep breaths and check in with yourself."
        }
    )