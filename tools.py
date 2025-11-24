
import json
from agents import function_tool
from agents.run_context import RunContextWrapper
from typing import Any

USER_PROFILE_FILE = "user_profile.json"

@function_tool
def read_user_profile(ctx: RunContextWrapper[Any]) -> dict:
    """
    Reads the user profile from the JSON file.
    Returns an empty dictionary if the file is not found.
    """
    try:
        with open(USER_PROFILE_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

@function_tool
def update_user_profile(ctx: RunContextWrapper[Any], key: str, value: str) -> dict:
    """
    Updates a specific key in the user profile and saves it to the JSON file.
    """
    # Since read_user_profile is now a tool, I can't call it directly.
    # I need to read the file manually here.
    try:
        with open(USER_PROFILE_FILE, "r") as f:
            profile = json.load(f)
    except FileNotFoundError:
        profile = {}
        
    profile[key] = value
    with open(USER_PROFILE_FILE, "w") as f:
        json.dump(profile, f, indent=4)
    return profile
