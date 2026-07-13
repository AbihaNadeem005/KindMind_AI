from backend.database.database import (
    create_tables,
    save_conversation
)

# Create the table
create_tables()

# Save one sample conversation
save_conversation(
    user_message="I failed my exam.",
    emotion="Sad",
    recommendation_title="Breathing Exercise",
    ai_response="I'm sorry to hear that. Take a deep breath and be kind to yourself."
)

print("Conversation saved successfully!")