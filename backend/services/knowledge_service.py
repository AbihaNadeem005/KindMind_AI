import json
import random
from pathlib import Path

# Project root (KindMind_AI)
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

# Data folder
DATA_DIR = PROJECT_ROOT / "data"


def load_json(filename):
    """
    Load a JSON file from the project's data folder.
    """

    file_path = DATA_DIR / filename

    print(f"Loading: {file_path}")   # Optional for debugging

    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)

# Load all knowledge once
quotes = load_json("quotes.json")
affirmations = load_json("affirmations.json")
breathing = load_json("breathing.json")
stories = load_json("stories.json")
music = load_json("music.json")


def get_quote(emotion):
    """
    Return a quote related to the detected emotion.
    """

    category_map = {
        "Happy": ["happiness", "gratitude"],
        "Excited": ["motivation", "confidence"],
        "Sad": ["hope", "kindness"],
        "Anxious": ["anxiety", "peace"],
        "Stressed": ["stress", "wellness"],
        "Angry": ["peace", "kindness"],
        "Neutral": ["motivation", "growth"]
    }

    categories = category_map.get(emotion, ["motivation"])

    matching = [
        quote
        for quote in quotes
        if quote["category"] in categories
    ]

    if matching:
        return random.choice(matching)["text"]

    return random.choice(quotes)["text"]


def get_affirmation(emotion):
    """
    Return an affirmation based on emotion.
    """

    category_map = {
        "Happy": ["gratitude", "happiness"],
        "Excited": ["motivation", "confidence"],
        "Sad": ["growth", "peace"],
        "Anxious": ["anxiety"],
        "Stressed": ["stress"],
        "Angry": ["peace"],
        "Neutral": ["motivation"]
    }

    categories = category_map.get(emotion, ["motivation"])

    matching = [
        item
        for item in affirmations
        if item["category"] in categories
    ]

    if matching:
        return random.choice(matching)["text"]

    return random.choice(affirmations)["text"]


def get_story():
    """
    Return one calming story.
    """

    return random.choice(stories)


def get_breathing_exercise():
    """
    Return one breathing exercise.
    """

    return random.choice(breathing)


def get_music(emotion):
    """
    Return music suggestion based on emotion.
    """

    matching = [
        item
        for item in music
        if item["emotion"] == emotion
    ]

    if matching:
        return random.choice(matching)

    return random.choice(music)