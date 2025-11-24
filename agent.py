
import os
from openai import AsyncOpenAI # Import AsyncOpenAI
from agents import Agent
from agents.models.openai_chatcompletions import OpenAIChatCompletionsModel
from tools import read_user_profile, update_user_profile

# Load API key from environment
api_key = os.getenv("GEMINI_API_KEY")

# Configure the AsyncOpenAI client for Gemini
openai_client = AsyncOpenAI( # Use AsyncOpenAI
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# Define Gemini model
gemini_model = OpenAIChatCompletionsModel(
    openai_client=openai_client,
    model="gemini-2.5-flash", # Reverting to 1.5-flash as it's more standard
)

# Define the system prompt
system_prompt = "Greet users by name if known. Detect when users share personal info and save it using tools."

# Create the agent
agent = Agent(
    name="Chatbot",
    instructions=system_prompt,
    model=gemini_model,
    tools=[read_user_profile, update_user_profile],
)
