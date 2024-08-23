from moviepy import editor
from openai import OpenAI
import openai_keys
import os
from datetime import timedelta
from moviepy.video.tools.subtitles import SubtitlesClip

client = OpenAI (
    api_key = openai_keys.api_key
)
TEXT_TO_SPEAK = "Am I the asshole for saying it's my birthday over and over again? sdsdsdsds dsdsds dsdsd sdsdsd sdsdsd sdsdsd sdsds sdsds dsds dsd sd sd sds ds dssdsdsd s dsdsds dsdsd"

def annotate(clip, txt, txt_color='white', fontsize=80, font='Roboto-Black'):
    txtclip = editor.TextClip(txt, fontsize=fontsize, font=font, color=txt_color, stroke_color='black', stroke_width=4)
    cvc = editor.CompositeVideoClip([clip, txtclip.set_pos(('center', 'center'))])
    return cvc.set_duration(clip.duration)

#pass in the text without the title. Then when we create the actual voiceover we pass in the entire text
def create_subs(start, words):
    subs = []
    for i in range(len(words)):
        if (words[i]["start"] >= start):
            s = words[i]["start"]
            e = words[i]["end"]
            s = str(0) + str(timedelta(seconds=(words[i]["start"])))
            e = str(0) + str(timedelta(seconds=(words[i]["end"])))
            if i + 1 < len(words):
                e = words[i + 1]["start"]
            text = words[i]["word"]

            word_id = i + 1
            segment = f"{word_id}\n{s} --> {e}\n{text[1:] if text[0] == ' ' else text}\n\n"
            with open("temp.srt", "a", encoding="utf-8") as f:
                f.write(segment)

def subtitle_video(subs, clip_num, start):
    video = editor.VideoFileClip(f"clips/clip_{clip_num}.mp4")
    annotated_clips = []
    annotated_clips.append(video.subclip(0, start))
    print("annotating")
    annotated_clips += [annotate(video.subclip(from_t, to_t), txt) for (from_t, to_t), txt in subs]
    print("concatenating")
    final_clip = editor.concatenate_videoclips(annotated_clips)
    print("writing")
    final_clip.write_videofile(f"temp_vid.mp4", fps=24, threads=32)


def get_transcript_words():
    audio_file = open("temp_audio.mp3", "rb")
    transcription = client.audio.transcriptions.create(
            model="whisper-1", 
            file=audio_file, 
            response_format="verbose_json",
            timestamp_granularities=['word']
        )
    return transcription.words

def main():
    subtitle_video(7)

if __name__ == "__main__":
    main()
