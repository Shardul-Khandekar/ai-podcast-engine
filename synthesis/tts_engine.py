import asyncio
import edge_tts
from pydub import AudioSegment
import os

# Define host personas
voices = {
    "Lucy": "en-US-JennyNeural",
    "Ken": "en-US-GuyNeural"
}



async def generate_podcast_audio(script_text, output_path="data/future_bytes_episode.mp3"):
    """
    Converts text to speech using Microsoft's neural voices.
    """
    print("Starting text-to-speech conversion...")
    combined_audio = AudioSegment.empty()

    # Split the script into segments for each host
    lines = script_text.strip().split('\n')

    for i, line in enumerate(lines):
        if not line.strip(): continue

        # Initialize default speaker
        speaker = "Lucy"
        clean_text = line

        if line.startswith("Lucy:"):
            speaker = "Lucy"
            clean_text = line.replace("Lucy:", "").strip()
        elif line.startswith("Ken:"):
            speaker = "Ken"
            clean_text = line.replace("Ken:", "").strip()

        temp_file = f"data/temp_{i}.mp3"
        communicate = edge_tts.Communicate(clean_text, voices[speaker])
        await communicate.save(temp_file)

        line_audio = AudioSegment.from_mp3(temp_file)
        combined_audio += line_audio + AudioSegment.silent(duration=300)

        os.remove(temp_file)

    combined_audio.export(output_path, format="mp3")
    print(f"Podcast complete! Saved to: {output_path}")


if __name__ == "__main__":
    sample_text = "Welcome to our podcast! Today we will explore the fascinating world of text-to-speech technology."
    asyncio.run(generate_podcast_audio(sample_text))