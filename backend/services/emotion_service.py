"""
Emotion Detection Service

Uses:
1. Special phrase detection (highest priority)
2. Keyword scoring
3. Neutral fallback
"""

def detect_emotion(user_message: str) -> str:

    message = user_message.lower().strip()

    # -----------------------------
    # Greetings
    # -----------------------------

    greetings = [
        "hi",
        "hello",
        "hey",
        "good morning",
        "good afternoon",
        "good evening"
    ]

    if any(message.startswith(word) for word in greetings):
        return "Neutral"

    # -----------------------------
    # Farewell
    # -----------------------------

    farewells = [
        "bye",
        "goodbye",
        "see you",
        "take care",
        "good night"
    ]

    if any(word in message for word in farewells):
        return "Neutral"

    # -----------------------------
    # Gratitude
    # -----------------------------

    gratitude = [
        "thanks",
        "thank you",
        "thankyou",
        "appreciate it"
    ]

    if any(word in message for word in gratitude):
        return "Happy"

    # =====================================================
    # SPECIAL RULES (Highest Priority)
    # =====================================================

    # Failed exam / interview
    if (
        ("fail" in message or "failed" in message)
        and (
            "exam" in message
            or "test" in message
            or "interview" in message
            or "result" in message
        )
    ):
        return "Sad"

    # Passed exam / selected / promotion
    if (
        any(word in message for word in [
            "passed",
            "selected",
            "promotion",
            "promoted",
            "won",
            "winner",
            "highest marks",
            "topper",
            "good marks",
            "excellent marks",
            "secured highest",
            "secured the highest",
            "distinction",
            "project works",
            "project is working",
            "project worked",
            "finally worked",
            "it worked",
            "it works"
        ])
    ):
        return "Excited"

    # Interview tomorrow / exam tomorrow
    if (
        (
            "exam" in message
            or "interview" in message
            or "presentation" in message
        )
        and
        any(word in message for word in [
            "tomorrow",
            "next week",
            "next month",
            "soon"
        ])
    ):
        return "Anxious"

    # Can't sleep
    if "can't sleep" in message or "cannot sleep" in message:
        return "Anxious"

    # Work stress
    if (
        any(word in message for word in [
            "office",
            "boss",
            "deadline",
            "deadlines",
            "workload",
            "burnout",
            "burned out"
        ])
    ):
        return "Stressed"

    # =====================================================
    # Keyword Scoring
    # =====================================================

    emotion_keywords = {

        "Happy": [

            "happy",
            "glad",
            "joy",
            "joyful",
            "wonderful",
            "great",
            "awesome",
            "cheerful",
            "pleased",
            "content",
            "grateful",
            "thankful",
            "fantastic",
            "good",
            "blessed",
            "relieved",
            "peaceful",
            "smile"

        ],

        "Excited": [

            "excited",
            "thrilled",
            "achievement",
            "achieved",
            "success",
            "successful",
            "completed",
            "finished",
            "promotion",
            "selected",
            "winner",
            "won",
            "graduated",
            "offer",
            "internship",
            "finally",
            "amazing",
            "highest",
            "marks",
            "secured",
            "celebrate",
            "celebration",
            "proud"

        ],

        "Sad": [

            "sad",
            "cry",
            "crying",
            "depressed",
            "failure",
            "upset",
            "heartbroken",
            "unhappy",
            "lonely",
            "hopeless",
            "worthless",
            "grief",
            "rejected",
            "broken",
            "disappointed",
            "miss"

        ],

        "Angry": [

            "angry",
            "mad",
            "furious",
            "annoyed",
            "hate",
            "frustrated",
            "irritated",
            "rage",
            "fed up",
            "unfair"

        ],

        "Anxious": [

            "anxious",
            "nervous",
            "worried",
            "panic",
            "panic attack",
            "fear",
            "afraid",
            "scared",
            "overthinking",
            "overthink",
            "uncertain"

        ],

        "Stressed": [

            "stressed",
            "stress",
            "pressure",
            "overwhelmed",
            "busy",
            "assignment",
            "assignments",
            "deadline",
            "deadlines",
            "workload",
            "office",
            "boss",
            "burnout",
            "burned out",
            "tired",
            "exhausted",
            "fatigue",
            "mental load",
            "too much work",
            "bored"

        ]

    }

    scores = {}

    for emotion, keywords in emotion_keywords.items():

        score = 0

        for keyword in keywords:

            if keyword in message:
                score += 1

        scores[emotion] = score

    print("\nEmotion Scores:")
    print(scores)

    detected = max(scores, key=scores.get)

    if scores[detected] == 0:
        return "Neutral"

    return detected