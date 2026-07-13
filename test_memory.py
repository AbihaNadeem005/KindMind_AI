from backend.database.database import get_recent_conversations

memory = get_recent_conversations()

print("\nRecent Conversations:\n")

for conversation in memory:
    print(conversation)