import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

# Create Gemini client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def detect_emotion(user_message: str) -> str:
    """
    Detects the user's emotion using Gemini.
    Returns only one emotion.
    """

    prompt = f"""
Analyze the following user message.

Return ONLY one emotion from this list:

Happy
Sad
Angry
Anxious
Stressed
Neutral
Excited

User Message:
"{user_message}"

Return only the emotion name.
"""

    try:
        response = client.models.generate_content(
            model="gemini-flash-latest",
            contents=prompt
        )

        return response.text.strip()

    except Exception as e:
        print(f"Emotion Detection Error: {e}")

        # Fallback emotion if Gemini is unavailable
        return "Neutral"