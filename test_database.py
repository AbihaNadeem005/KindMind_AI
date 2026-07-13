from backend.database.database import (
    create_tables,
    save_conversation,
    get_all_conversations
)

# Create the table
create_tables()

# Save a sample conversation
save_conversation(
    user_message="I got selected in my interview!",
    emotion="Excited",
    recommendation_title="Achievement Journal",
    ai_response="Congratulations! You should celebrate your success."
)

# Retrieve all conversations
conversations = get_all_conversations()

print("\nStored Conversations:\n")

for conversation in conversations:
    print(conversation)