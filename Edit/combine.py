import ffmpeg
import requests
import json
import os
from . import eleven_keys
# Define constants for the script
CHUNK_SIZE = 1024  # Size of chunks to read/write at a time
XI_API_KEY = eleven_keys.XI  # Your API key for authentication
VOICE_ID = eleven_keys.ANTONI # ID of the voice model to use
TEXT_TO_SPEAK = "Am I the asshole for saying it's my birthday over and over again?"  # Text you want to convert to speech
OUTPUT_PATH = "output.mp3"  # Path to save the output audio file

def create_audio(text, out_path):
    tts_url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}/stream"
    headers = {
        "Accept": "application/json",
        "xi-api-key": XI_API_KEY
    }
    data = {
        "text": text,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.8,
            "style": 0.0,
            "use_speaker_boost": True
        }
    }

    response = requests.post(tts_url, headers=headers, json=data, stream=True)
    
    if response.ok:
    # Open the output file in write-binary mode
        with open(out_path, "wb") as f:
        # Read the response in chunks and write to the file
            for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
                f.write(chunk)
        # Inform the user of success
        print("Audio stream saved successfully.")
    else:
    # Print the error message if the request was not successful
        print(response.text)

def merge_audio(audio_path, video_path, out_path):
    # get the duration of the audio file
    duration = ffmpeg.probe(audio_path)["format"]["duration"]
    # trim the video file to match the duration of the audio file
    ffmpeg.input(video_path).output("tma.mp4", t=duration).run()
    #get both to be combined
    input_video = ffmpeg.input("tma.mp4")
    added_audio = ffmpeg.input(audio_path).audio #.filter('adelay', "1500|1500")
    # combine the two inputs
    (
        ffmpeg
        .concat(input_video, added_audio, v=1, a=1)
        .output(out_path)
        .run(overwrite_output=True)
    )   
    if os.path.exists("tma.mp4"):
        os.remove ("tma.mp4")

def main():
    #create_audio(TEXT_TO_SPEAK, "testing_audio.mp3")
    merge_audio("testing_audio.mp3", "test_2.mp4", "testing_video.mp4")

if __name__ == "__main__":
    main()
