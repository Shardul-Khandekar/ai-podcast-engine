import asyncio
from agents.scriptwriter import script_agent

async def test_script():
    print("Starting Scriptwriter Agent Test...")
    
    # Simulated research input
    mock_research = """
        1. NVIDIA's new Blackwell chips are 30x faster.
        2. Apple is integrating AI into the calculator app.
        3. Scientists used AI to communicate with a whale.
    """

    print("Feeding research to Scriptwriter Agent...")
    response = await script_agent.run(mock_research)
    print("Agent Response:")
    print(response)

if __name__ == "__main__":
    asyncio.run(test_script())