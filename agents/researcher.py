import os
from agent_framework import ChatAgent
from agent_framework.openai import OpenAIChatClient
from dotenv import load_dotenv

load_dotenv()

# Initialize OpenAI chat client
client = OpenAIChatClient(
    model_id="gpt-4o",
    api_key=os.getenv("OPENAI_API_KEY")
)

# Define researcher persona
researcher_persona = """
    You are the Lead Researcher for the 'Future Bytes' podcast. 
    Your goal is to find the most interesting and trending news about the topic the user is interested in.
    When asked to research a topic:
    1. Identify 3 key news items.
    2. Provide a brief summary of why each is important.
    3. Suggest a 'hook' or angle for a podcast episode.
    Keep your tone professional yet curious.
"""

# Create agent instance
researcher_agent = ChatAgent(
    chat_client=client,
    name="TrendFinder",
    instructions=researcher_persona
)