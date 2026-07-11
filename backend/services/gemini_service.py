import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

# Create the Gemini client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def get_gemini_response(user_message: str) -> str:
    """
    Sends the user's message to Gemini
    and returns only the generated text.
    """

    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=user_message
    )

    return response.text