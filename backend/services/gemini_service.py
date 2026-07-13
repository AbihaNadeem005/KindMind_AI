import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def get_gemini_response(
    user_message: str,
    emotion: str,
    recommendation: dict
) -> str:

    prompt = f"""
You are KindMind AI, a supportive mental wellness assistant.

The user's detected emotion is: {emotion}

The recommended wellness activity is:
Title: {recommendation['title']}
Category: {recommendation['category']}
Description: {recommendation['description']}

The user said:
"{user_message}"

Respond with empathy.

Naturally encourage the user to try the recommended activity.

Keep the response supportive, warm, and conversational.
"""

    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=prompt
    )

    return response.text