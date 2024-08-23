from Source import reddit_keys, reddit
from Edit import subs, combine, thumbnail, audio
import random, shlex
import os
from Upload import Tiktok_uploader
import ffmpeg
import moviepy.editor as mpy
from moviepy.video.fx.all import crop

def create_tiktoks(num_videos):
    vids = reddit.get_posts(num_videos)
    
    vid_num = 4
    for key in vids:
        #replace aita 
        text = key.replace("AITA", "Am I the aye hole") + vids[key]
        #get random number for video
        clip_num = random.randrange(1, 8)
        #first we create the audio for the video
        audio.create_audio(text)
        #then we get the words with associated timestamps
        words = subs.get_transcript_words()
        #then we calculate the delay for the subtitles to start
        delay = calculate_delay(words, key)
        #then we create the subtitles for the video, excluding the title
        subtitles = subs.create_subs(delay, words)
        #then we burn the subtitles onto a video
        subs.subtitle_video(subtitles, 7, delay)
        #then we create the thumbnail
        thumbnail.create_thumbnail(key)
        #then we add it to the video
        thumbnail.add_thumb("temp_vid.mp4", "temp_thumbnail.png", delay)
        #then we combine the audio and the video
        combine.merge_audio("temp_audio.mp3", "temp_vid_thumb.mp4", "cropped_video.mp4")

        clip = mpy.VideoFileClip("cropped_video.mp4")
        (w, h) = clip.size

        crop_width = h * 9/16
        # x1,y1 is the top left corner, and x2, y2 is the lower right corner of the cropped area.

        x1, x2 = (w - crop_width)//2, (w+crop_width)//2
        y1, y2 = 0, h
        cropped_clip = crop(clip, x1=x1, y1=y1, x2=x2, y2=y2)
        # or you can specify center point and cropped width/height
        # cropped_clip = crop(clip, width=crop_width, height=h, x_center=w/2, y_center=h/2)
        cropped_clip.write_videofile(f"tiktoks/tiktok_{vid_num}.mp4")
        # if os.path.exists("temp_thumbnail.png"):
        #    os.remove("temp_thumbnail.png")
        # if os.path.exists("temp_audio.mp3"):
        #     os.remove("temp_audio.mp3")
        # if os.path.exists("temp_vid_thumb.mp4"):
        #     os.remove("temp_vid_thumb.mp4")
        vid_num += 1
    

    

def calculate_delay(words, key):
    key = key.replace("'", "\\'")
    i = len(shlex.split(key)) + 4

    print(i)
    for word in words:
        s = word["start"]
        e = word["end"]
        text = word["word"]
        print(f"word: {text} start: {s} end: {e}")
        if i <= 1:
            return word["end"]
        i -= 1

    return 0


        

def main():
    #create_tiktoks(1)
    # test = "Testing the whispers subtitle methods."
    # words = subs.get_transcript_words()
    # delay = calculate_delay(words, test)
    # subtitles = subs.create_subs(delay, words)
    # subs.subtitle_video(subtitles, 1, 2, delay)
    #     #then we create the thumbnail
    # thumbnail.create_thumbnail(test)
    #     #then we add it to the video
    # thumbnail.add_thumb("temp_vid.mp4", "temp_thumbnail.png", delay)

    # combine.merge_audio("testing_audio.mp3", "temp_vid_thumb.mp4", f"tiktoks/tiktok_{2}.mp4")
    # print()
    # print(delay)
    #Tiktok_uploader.schedule_and_upload_videos()
    create_tiktoks(1)
    
            
if __name__ == "__main__":
    main()