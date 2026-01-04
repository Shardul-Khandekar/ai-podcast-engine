import asyncio
from agents.researcher import researcher_agent
from agents.scriptwriter import script_agent
from agent_framework import SequentialBuilder, WorkflowOutputEvent
import os

async def run_podcast_studio(topic):
    print(f"Starting 'Future Bytes' Studio for topic: {topic}")

    # Define the workflow
    workflow = (
        SequentialBuilder()
        .participants([researcher_agent, script_agent])
        .build()
    )

    # Run the workflow
    async for event in workflow.run_stream(f"{topic}"):
        if isinstance(event, WorkflowOutputEvent):
            if isinstance(event.data, list):
                last_message = event.data[-1]
                if hasattr(last_message, 'text'):
                    final_script = last_message.text
                else:
                    final_script = last_message.contents[0].text
            else:
                final_script = str(event.data)

    if final_script:
        print("Final Podcast Script:")
        print(final_script)

        os.makedirs("data", exist_ok=True)
        with open("data/podcast_script.txt", "w") as f:
            f.write(final_script)
    else:
        print("Failed to extract script from workflow output.")

    return final_script

if __name__ == "__main__":
    topic = "The rise of local-first AI models"
    asyncio.run(run_podcast_studio(topic))