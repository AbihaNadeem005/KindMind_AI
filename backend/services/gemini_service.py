import os
import time

from dotenv import load_dotenv
from google import genai

from backend.database.database import get_recent_conversations
from backend.services.knowledge_service import (
    get_quote,
    get_affirmation,
    get_story,
    get_breathing_exercise,
    get_music
)
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)


def get_gemini_response(
    user_message: str,
    emotion: str,
    recommendation: dict,
    comfort_plan: list,
    home_wellness: dict
) -> str:
    """
    Generates an empathetic response using Gemini
    while considering previous conversations.
    """

    # Retrieve previous conversations
    recent_memories = get_recent_conversations(3)

    if recent_memories:

        memory_text = ""

        for i, (message, past_emotion, ai_response) in enumerate(
            recent_memories,
            start=1
        ):

            memory_text += f"""
Conversation {i}

User:
{message}

Emotion:
{past_emotion}

Assistant:
{ai_response}

----------------------------------------
"""

    else:

        memory_text = "No previous conversations."

    # Debug
    print("\n========== MEMORY ==========")
    print(memory_text)
    print("============================\n")

    quote = get_quote(emotion)

    affirmation = get_affirmation(emotion)

    story = get_story()

    breathing = get_breathing_exercise()

    music = get_music(emotion)

    prompt = f"""
You are KindMind AI.

You are a compassionate AI mental wellness assistant.

You are continuing an ongoing conversation with the same user.

The information below contains previous conversations with this user.

Use these memories naturally whenever they are relevant.

Do NOT mention that you have memory or access to previous conversations.

Do NOT say things like:
"I checked our previous chats."

Instead, respond naturally like a caring friend.

------------------------------------------------

PREVIOUS CONVERSATIONS

{memory_text}

------------------------------------------------
------------------------------------------------

KNOWLEDGE

Motivational Quote:
{quote}

Affirmation:
{affirmation}

Breathing Exercise:
{breathing['title']}

Music Suggestion:
{music['suggestion']}

Story:
{story['story']}

------------------------------------------------

CURRENT USER EMOTION

{emotion}

------------------------------------------------

RECOMMENDED WELLNESS ACTIVITY

Title:
{recommendation['title']}

Category:
{recommendation['category']}

Description:
{recommendation['description']}

------------------------------------------------

COMFORT PLAN

{chr(10).join(f"- {step}" for step in comfort_plan)}

------------------------------------------------

HOME WELLNESS MODE

Lighting:
{home_wellness['lighting']}

Sound:
{home_wellness['sound']}

Environment:
{home_wellness['environment']}

Device:
{home_wellness['device']}

------------------------------------------------

CURRENT USER MESSAGE

{user_message}

------------------------------------------------

Instructions

- Be warm, empathetic and supportive.
- Validate the user's emotions.
- Use previous conversations only when they naturally help the conversation.
- Never force references to old conversations.
- If the user starts a completely new topic, focus on the new topic.
- Encourage the recommended wellness activity naturally.
- Avoid repeating the exact same advice from previous conversations unless it is still helpful.
- Keep the response conversational and human-like.
- End with a gentle question or encouraging sentence whenever appropriate.
- If appropriate, naturally include one or two steps from the comfort plan.
- Do not list the entire comfort plan unless it genuinely helps the user.
- If appropriate, naturally suggest one or two home wellness ideas.
- Do not list every suggestion unless it genuinely helps.
- Blend the suggestions naturally into the conversation.
- When appropriate, naturally include the motivational quote.
- When appropriate, naturally include the affirmation.
- If the user asks to relax, use the breathing exercise.
- If the user asks for a story, use the provided story.
- If music would help, suggest the provided music recommendation.
- Do not force all of these into every response. Use only what fits the conversation naturally.
"""

    # Retry Gemini up to 3 times if the server is busy
    for attempt in range(3):

        try:

            response = client.models.generate_content(
                model="gemini-flash-latest",
                contents=prompt
            )

            return response.text

        except Exception as e:

            error_message = str(e)

            # Retry only for temporary server overload
            if "503" in error_message or "UNAVAILABLE" in error_message:

                print(f"Gemini busy... Retrying ({attempt + 1}/3)")

                time.sleep(2)

                continue

            # Any other error
            print(f"Gemini Error: {e}")

            return (
                "I'm sorry, I'm having trouble connecting to the AI service right now. "
                "Please try again in a few moments."
            )

    # If all retries fail
    return (
        "The AI service is currently experiencing high demand. "
        "Please try again in a few moments."
    )