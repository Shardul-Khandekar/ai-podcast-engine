import asyncio
import edge_tts

async def generate_podcast_audio(text, voice="en-US-GuyNeural", filename="output.mp3"):
    """
    Converts text to speech using Microsoft's neural voices.
    """
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(f"data/{filename}")
    print(f"Audio saved to data/{filename}")

if __name__ == "__main__":
    sample_text = "Welcome to our podcast! Today we will explore the fascinating world of text-to-speech technology."
    asyncio.run(generate_podcast_audio(sample_text))