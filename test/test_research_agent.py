import asyncio
from agents.researcher import researcher_agent

async def test_agent():
    print("Starting Research Agent Test...")
    response = await researcher_agent.run("Research the latest trends in AI related for podcasts")
    print("Agent Response:")
    print(response)

if __name__ == "__main__":
    asyncio.run(test_agent())