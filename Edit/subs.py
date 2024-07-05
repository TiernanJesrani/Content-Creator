from moviepy import editor
TEXT_TO_SPEAK = "Am I the asshole for saying it's my birthday over and over again? sdsdsdsds dsdsds dsdsd sdsdsd sdsdsd sdsdsd sdsds sdsds dsds dsd sd sd sds ds dssdsdsd s dsdsds dsdsd"

def annotate(clip, txt, txt_color='white', fontsize=100, font='Roboto-Black'):
    print("a")
    txtclip = editor.TextClip(txt, fontsize=fontsize, font=font, color=txt_color, stroke_color='black', stroke_width=4)
    cvc = editor.CompositeVideoClip([clip, txtclip.set_pos(('center', 'center'))])
    return cvc.set_duration(clip.duration)

#pass in the text without the title. Then when we create the actual voiceover we pass in the entire text
def create_subs(txt, start):
    subs = []
    i = start
    for word in txt.split():
        subs.append(((i, i + 0.33), word))
        i = i + 0.33
    return subs

def subtitle_video(subs, clip_num, vid_num, start):
    video = editor.VideoFileClip(f"clips/clip_{clip_num}.mp4")
    annotated_clips = []
    annotated_clips.append(video.subclip(0, start))
    print("annotating")
    annotated_clips += [annotate(video.subclip(from_t, to_t), txt) for (from_t, to_t), txt in subs]
    print("concatenating")
    final_clip = editor.concatenate_videoclips(annotated_clips)
    print("writing")
    final_clip.write_videofile(f"temp_vid.mp4", fps=24, threads=32)
    

def main():
    #print(editor.TextClip.list("font"))
   subs = create_subs(TEXT_TO_SPEAK, 1)
   subtitle_video(subs, 2, 1, 1)

if __name__ == "__main__":
    main()
