# utils/file_storage.py
import json, os

DATA_FILE = "user_data/user_profiles.json"


def save_user_profile(username, sentence, voice_path):
    data = {}

    # Load existing data if available
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                pass

    # Update or add the user profile
    data[username] = {
        "sentence": sentence,
        "voice_path": voice_path
    }

    # Ensure directory exists
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)

    # Save updated data
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


def load_user_profile(username):
    if not os.path.exists(DATA_FILE):
        return None
    with open(DATA_FILE, "r") as f:
        data = json.load(f)
    return data.get(username)
