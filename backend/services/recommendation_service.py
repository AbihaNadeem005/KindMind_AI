import random


def get_recommendation(emotion: str) -> dict:
    """
    Returns a personalized wellness recommendation
    based on the detected emotion.
    """

    recommendations = {

        "Happy": [

            {
                "title": "Gratitude Journal",
                "category": "Reflection",
                "description": "Write down three things you are grateful for today."
            },

            {
                "title": "Celebrate Your Success",
                "category": "Reflection",
                "description": "Take a moment to appreciate today's positive moments."
            },

            {
                "title": "Share Your Happiness",
                "category": "Social",
                "description": "Share your good news with someone you care about."
            }

        ],

        "Excited": [

            {
                "title": "Achievement Journal",
                "category": "Reflection",
                "description": "Write about today's achievements and celebrate your progress."
            },

            {
                "title": "Capture the Moment",
                "category": "Reflection",
                "description": "Write about what made today exciting so you can remember it."
            },

            {
                "title": "Victory Walk",
                "category": "Activity",
                "description": "Take a short walk while reflecting on your accomplishment."
            }

        ],

        "Sad": [

            {
                "title": "Breathing Exercise",
                "category": "Relaxation",
                "description": "Take five slow deep breaths to calm your mind."
            },

            {
                "title": "Listen to Soft Music",
                "category": "Music",
                "description": "Play calming instrumental music for a few minutes."
            },

            {
                "title": "Write Your Feelings",
                "category": "Journaling",
                "description": "Express your thoughts freely in a journal."
            }

        ],

        "Angry": [

            {
                "title": "Progressive Muscle Relaxation",
                "category": "Relaxation",
                "description": "Slowly tense and relax your muscles."
            },

            {
                "title": "Take a Short Walk",
                "category": "Activity",
                "description": "Walk for ten minutes to release built-up tension."
            },

            {
                "title": "Deep Breathing",
                "category": "Relaxation",
                "description": "Practice slow breathing before reacting."
            }

        ],

        "Anxious": [

            {
                "title": "Mindfulness Meditation",
                "category": "Meditation",
                "description": "Spend five minutes focusing on your breathing."
            },

            {
                "title": "Grounding Exercise",
                "category": "Mindfulness",
                "description": "Practice the 5-4-3-2-1 grounding technique."
            },

            {
                "title": "Positive Affirmations",
                "category": "Reflection",
                "description": "Repeat a few calming and encouraging affirmations."
            }

        ],

        "Stressed": [

            {
                "title": "Nature Sounds",
                "category": "Music",
                "description": "Listen to calming rainfall or forest sounds."
            },

            {
                "title": "Stretch Break",
                "category": "Activity",
                "description": "Take five minutes to stretch your body."
            },

            {
                "title": "Tea Break",
                "category": "Relaxation",
                "description": "Step away from work and enjoy a warm drink."
            }

        ],

        "Neutral": [

            {
                "title": "Short Walk",
                "category": "Activity",
                "description": "Take a short walk and enjoy some fresh air."
            },

            {
                "title": "Read Something Inspiring",
                "category": "Reading",
                "description": "Spend a few minutes reading something uplifting."
            },

            {
                "title": "Hydration Break",
                "category": "Self-Care",
                "description": "Drink a glass of water and take a short pause."
            }

        ]
    }

    default_recommendation = {
        "title": "Deep Breathing",
        "category": "Relaxation",
        "description": "Take a few deep breaths and check in with yourself."
    }

    return random.choice(
        recommendations.get(
            emotion,
            [default_recommendation]
        )
    )