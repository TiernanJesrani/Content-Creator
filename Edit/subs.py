from moviepy import editor
TEXT_TO_SPEAK = "Am I the asshole for saying it's my birthday over and over again?"

def annotate(clip, txt, txt_color='black', fontsize=50, font='Chalkboard'):
    txtclip = editor.TextClip(txt, fontsize=fontsize, font=font, color=txt_color, stroke_color='white', stroke_width=2)
    cvc = editor.CompositeVideoClip([clip, txtclip.set_pos(('center', 'center'))])
    return cvc.set_duration(clip.duration)

def create_subs(txt):
    subs = []
    i = 0
    for word in txt.split():
        subs.append(((i, i + 0.2), word))
        i = i + 0.2
    return subs

def main():
    video = editor.VideoFileClip("vid.mp4")
    subs = create_subs(TEXT_TO_SPEAK)
    annotated_clips = [annotate(video.subclip(from_t, to_t), txt) for (from_t, to_t), txt in subs]
    final_clip = editor.concatenate_videoclips(annotated_clips)
    final_clip.write_videofile("test_2.mp4")

if __name__ == "__main__":
    main()
