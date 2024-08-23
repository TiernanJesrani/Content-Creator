from unrealspeech import UnrealSpeechAPI, play, save
from . import unreal_speech_keys

def create_audio(text):
    speech_api = UnrealSpeechAPI(unreal_speech_keys.API_KEY)

    text_to_speech = text
    timestamp_type = "sentence" 
    voice_id = unreal_speech_keys.VOICE  
    bitrate = "192k"
    speed = .25 
    pitch = 1.0
    #audio_data = speech_api.speech(text=text_to_speech,voice_id=voice_id, bitrate=bitrate, timestamp_type=timestamp_type, speed=speed, pitch=pitch)
    # Create a synthesis task
    task_id = speech_api.create_synthesis_task(text=text_to_speech, voice_id=voice_id, bitrate="320k", timestamp_type="word", speed=0.25, pitch=1.0)

    #Check the task status
    audio_data = speech_api.get_synthesis_task_status(task_id)

    save(audio_data, "temp_audio.mp3")

# Play audio
def main():
    create_audio("test")

if __name__ == "__main__":
    main()