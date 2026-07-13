from backend.database.database import get_all_conversations

conversations = get_all_conversations()

print("\nStored Conversations:\n")

for conversation in conversations:
    print(conversation)