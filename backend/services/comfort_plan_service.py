import random


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
            "Listen to calming music.",
            "Watch your favorite comfort movie.",
            "Wrap yourself in a cozy blanket.",
            "Take a warm cup of tea.",
            "Go outside for a few minutes.",
            "Write about your feelings in a journal.",
            "Remember one happy memory."

        ],

        "Anxious": [

            "Practice a five-minute breathing exercise.",
            "Drink a glass of water.",
            "Focus on one task at a time.",
            "Take a short break from screens.",
            "Try the 5-4-3-2-1 grounding technique.",
            "Stretch your shoulders and neck.",
            "Slow your breathing for one minute.",
            "Take a short walk.",
            "Repeat a calming affirmation.",
            "Close your eyes and relax for two minutes."

        ],

        "Stressed": [

            "Stretch your body for five minutes.",
            "Take a short walk.",
            "Listen to calming music.",
            "Get some fresh air.",
            "Pause your work for five minutes.",
            "Drink a glass of water.",
            "Reduce your screen brightness.",
            "Organize one small task first.",
            "Practice mindful breathing.",
            "Relax your shoulders."

        ],

        "Happy": [

            "Celebrate today's success.",
            "Share your happiness with someone.",
            "Write today's positive moment in a journal.",
            "Capture a happy photo.",
            "Treat yourself to something nice.",
            "Spend time with loved ones.",
            "Express gratitude.",
            "Enjoy your favorite hobby.",
            "Take a relaxing walk.",
            "Smile and enjoy the moment."

        ],

        "Excited": [

            "Capture today's achievement in a journal.",
            "Celebrate your progress.",
            "Take a relaxing break before your next goal.",
            "Share your success with someone.",
            "Write down what you're most proud of.",
            "Reward yourself.",
            "Take some memorable photos.",
            "Reflect on how far you've come.",
            "Enjoy the moment before moving forward.",
            "Set your next exciting goal."

        ],

        "Angry": [

            "Pause before reacting.",
            "Take ten deep breaths.",
            "Go for a short walk.",
            "Write down what's bothering you.",
            "Count slowly to ten.",
            "Listen to calming music.",
            "Drink a glass of cold water.",
            "Stretch your muscles.",
            "Take a short break.",
            "Focus on slow breathing."

        ],

        "Neutral": [

            "Stay hydrated.",
            "Take a short walk.",
            "Spend a few minutes relaxing.",
            "Read something inspiring.",
            "Organize your workspace.",
            "Stretch your body.",
            "Take a deep breath.",
            "Listen to peaceful music.",
            "Open a window for fresh air.",
            "Take a mindful break."

        ]
    }

    default_plan = plans["Neutral"]

    selected_plan = plans.get(
        emotion,
        default_plan
    )

    return random.sample(
        selected_plan,
        k=min(4, len(selected_plan))
    )