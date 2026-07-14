def get_comfort_plan(emotion: str):
    """
    Returns a personalized comfort plan
    based on the detected emotion.
    """

    plans = {

        "Sad": [
            "Take five slow deep breaths.",
            "Write down one thing you're grateful for.",
            "Talk to someone you trust.",
            "Be kind to yourself today."
        ],

        "Anxious": [
            "Practice a five-minute breathing exercise.",
            "Drink a glass of water.",
            "Focus on one task at a time.",
            "Take a short break from screens."
        ],

        "Stressed": [
            "Stretch your body for five minutes.",
            "Take a short walk.",
            "Listen to calming music.",
            "Get some fresh air."
        ],

        "Happy": [
            "Celebrate today's success.",
            "Share your happiness with someone.",
            "Write today's positive moment in a journal."
        ],

        "Excited": [
            "Capture today's achievement in a journal.",
            "Celebrate your progress.",
            "Take a relaxing break before your next goal."
        ],

        "Angry": [
            "Pause before reacting.",
            "Take ten deep breaths.",
            "Go for a short walk.",
            "Write down what's bothering you."
        ],

        "Neutral": [
            "Stay hydrated.",
            "Take a short walk.",
            "Spend a few minutes relaxing."
        ]
    }

    return plans.get(
        emotion,
        plans["Neutral"]
    )