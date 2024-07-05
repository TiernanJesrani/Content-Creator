from Source import reddit_keys, reddit
from Edit import subs, eleven_keys, combine, thumbnail
import random, shlex
import os

def create_tiktoks(num_videos):
    vids = reddit.get_posts(num_videos)
    for key in vids:
        count = 0
        for word in vids[key].split():
           count += 1
        print (len(shlex.split(key)) + count)
    
    vid_num = 1
    for key in vids:
        #get random number for video
        clip_num = random.randrange(1, 8)
        #first we calculate the delay for the subtitles to start
        delay = 0.33 * len(shlex.split(key))
        #then we create the subtitles for the video, excluding the title
        subtitles = subs.create_subs(vids[key], 5)
        #then we burn the subtitles onto a video
        subs.subtitle_video(subtitles, 2, vid_num, 5)
        #then we create the thumbnail
        thumbnail.create_thumbnail(key)
        # #then we add it to the video
        thumbnail.add_thumb("temp_vid.mp4", "temp_thumbnail.png", delay)
        # #then we create the audio for the video
        text = key.replace("AITA", "Am I the aye hole") + vids[key]
        combine.create_audio(text, "temp_audio.mp3")
        #then we combine the audio and the video
        combine.merge_audio("temp_audio.mp3", "temp_vid_thumb.mp4", f"tiktoks/tiktok_{vid_num}.mp4")
        if os.path.exists("temp_thumbnail.png"):
           os.remove("temp_thumbnail.png")
        if os.path.exists("temp_audio.mp3"):
            os.remove("temp_audio.mp3")
        if os.path.exists("temp_vid_thumb.mp4"):
            os.remove("temp_vid_thumb.mp4")
    

    





        

def main():
    create_tiktoks(8)
        
if __name__ == "__main__":
    main()