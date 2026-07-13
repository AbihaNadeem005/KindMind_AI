import sqlite3
import os

DATABASE_NAME = "kindmind.db"


def get_connection():
    print("Database path:", os.path.abspath(DATABASE_NAME))

    connection = sqlite3.connect(DATABASE_NAME)

    return connection

def create_tables():
    """
    Creates the conversations table
    if it does not already exist.
    """

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS conversations (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        user_message TEXT NOT NULL,

        emotion TEXT NOT NULL,

        recommendation_title TEXT NOT NULL,

        ai_response TEXT NOT NULL,

        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP

    )
    """)

    connection.commit()

    connection.close()

def save_conversation(
    user_message,
    emotion,
    recommendation_title,
    ai_response
):
    """
    Saves one conversation into the database.
    """

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO conversations
        (
            user_message,
            emotion,
            recommendation_title,
            ai_response
        )
        VALUES (?, ?, ?, ?)
    """, (
        user_message,
        emotion,
        recommendation_title,
        ai_response
    ))

    
    connection.commit()

    connection.close()

def get_all_conversations():
    """
    Retrieves all conversations from the database.
    """

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT * FROM conversations
    """)

    conversations = cursor.fetchall()

    connection.close()

    return conversations
