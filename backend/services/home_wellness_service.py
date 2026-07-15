import random


def get_home_wellness_mode(emotion: str):
    """
    Returns personalized home wellness suggestions
    based on the detected emotion.
    """

    wellness = {

        "Sad": {

            "lighting": [
                "Open the curtains and let natural light in.",
                "Use warm lighting to create a cozy atmosphere.",
                "Sit near a window with natural daylight."
            ],

            "sound": [
                "Play uplifting instrumental music.",
                "Listen to calming piano music.",
                "Play soft acoustic music."
            ],

            "environment": [
                "Sit somewhere comfortable with a blanket.",
                "Open a window for fresh air.",
                "Spend a few minutes outside if possible."
            ],

            "device": [
                "Reduce unnecessary notifications.",
                "Take a short break from social media.",
                "Enable Focus Mode for a while."
            ]

        },

        "Anxious": {

            "lighting": [
                "Dim bright lights for a calmer atmosphere.",
                "Use warm bedside lighting.",
                "Reduce harsh screen brightness."
            ],

            "sound": [
                "Play soft nature sounds.",
                "Listen to rainfall or ocean waves.",
                "Play gentle piano music."
            ],

            "environment": [
                "Open a window for fresh air.",
                "Sit somewhere quiet.",
                "Keep your workspace tidy."
            ],

            "device": [
                "Enable Do Not Disturb mode.",
                "Mute unnecessary notifications.",
                "Take a short break from your phone."
            ]

        },

        "Stressed": {

            "lighting": [
                "Use warm lighting to reduce eye strain.",
                "Lower your screen brightness.",
                "Turn on soft ambient lighting."
            ],

            "sound": [
                "Play calming rainfall sounds.",
                "Listen to forest ambience.",
                "Play relaxing instrumental music."
            ],

            "environment": [
                "Take a short break away from your workspace.",
                "Stretch your body for a few minutes.",
                "Get some fresh air."
            ],

            "device": [
                "Mute work notifications for a few minutes.",
                "Close unnecessary applications.",
                "Enable Focus Mode while relaxing."
            ]

        },

        "Happy": {

            "lighting": [
                "Keep the room bright and cheerful.",
                "Enjoy natural daylight.",
                "Open the curtains."
            ],

            "sound": [
                "Play your favorite upbeat playlist.",
                "Listen to energetic music.",
                "Enjoy relaxing background music."
            ],

            "environment": [
                "Share your happiness with someone nearby.",
                "Take a walk outside.",
                "Celebrate your achievement."
            ],

            "device": [
                "Capture today's happy moment with a photo.",
                "Write today's success in a journal.",
                "Share your good news with someone."
            ]

        },

        "Excited": {

            "lighting": [
                "Keep your workspace bright and organized.",
                "Use bright natural lighting.",
                "Tidy your desk before your next task."
            ],

            "sound": [
                "Play energetic background music.",
                "Listen to inspiring instrumental music.",
                "Enjoy your favorite motivational playlist."
            ],

            "environment": [
                "Celebrate your achievement before moving on.",
                "Take a short walk.",
                "Reflect on today's success."
            ],

            "device": [
                "Take a picture of today's accomplishment.",
                "Write down your achievement.",
                "Share your success with someone."
            ]

        },

        "Angry": {

            "lighting": [
                "Reduce harsh lighting.",
                "Use soft warm lights.",
                "Dim bright screens."
            ],

            "sound": [
                "Play slow instrumental music.",
                "Listen to calming rainfall.",
                "Play peaceful ambient sounds."
            ],

            "environment": [
                "Step away from the current situation.",
                "Take a short walk.",
                "Spend a few quiet minutes alone."
            ],

            "device": [
                "Silence your phone.",
                "Mute notifications temporarily.",
                "Take a break from social media."
            ]

        },

        "Neutral": {

            "lighting": [
                "Keep your room comfortably lit.",
                "Open the curtains.",
                "Use comfortable natural lighting."
            ],

            "sound": [
                "Play soft ambient sounds.",
                "Listen to relaxing instrumental music.",
                "Enjoy gentle background music."
            ],

            "environment": [
                "Stretch and get some fresh air.",
                "Organize your workspace.",
                "Take a short mindful break."
            ],

            "device": [
                "Take a short break from screens.",
                "Drink some water before returning to work.",
                "Silence unnecessary notifications."
            ]

        }

    }

    selected = wellness.get(emotion, wellness["Neutral"])

    return {
        "lighting": random.choice(selected["lighting"]),
        "sound": random.choice(selected["sound"]),
        "environment": random.choice(selected["environment"]),
        "device": random.choice(selected["device"])
    }