import os
from dotenv import load_dotenv
from google import genai

from backend.database.database import get_recent_conversations

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def get_gemini_response(
    user_message: str,
    emotion: str,
    recommendation: dict
) -> str:

    # Retrieve the last 3 conversations
    recent_memories = get_recent_conversations(3)

    # Format previous conversations
    if recent_memories:
        memory_text = "Previous conversations:\n\n"

        for i, (message, past_emotion, _) in enumerate(recent_memories, start=1):
            memory_text += (
                f"{i}. User said: {message}\n"
                f"Detected emotion: {past_emotion}\n\n"
            )
    else:
        memory_text = "No previous conversations available."

    print("\n========== MEMORY ==========")
    print(memory_text)
    print("============================\n")

    prompt = f"""
You are KindMind AI, a supportive mental wellness assistant.

The user's detected emotion is:
{emotion}

{memory_text}

The recommended wellness activity is:

Title: {recommendation['title']}
Category: {recommendation['category']}
Description: {recommendation['description']}

Current user message:

"{user_message}"

Instructions:
- Use the previous conversations only if they are relevant.
- If appropriate, gently acknowledge something the user shared before.
- Do not mention the database or memory explicitly.
- Respond with empathy.
- Naturally encourage the recommended activity.
- Keep the response warm, supportive, and conversational.
"""

    try:
        response = client.models.generate_content(
            model="gemini-flash-latest",
            contents=prompt
        )

        return response.text

    except Exception as e:
        print(f"Gemini Error: {e}")

        return (
            "I'm sorry, I'm having trouble connecting to the AI service at the moment. "
            "Please try again in a few moments."
        )