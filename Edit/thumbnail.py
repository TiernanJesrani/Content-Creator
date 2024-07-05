from PIL import Image, ImageFont, ImageDraw
from moviepy import editor
from moviepy.video.fx.all import resize

def create_thumbnail(title):
    font = ImageFont.truetype('/Library/Fonts/Inter-Bold.ttf', 30)
    img = Image.open("Template.png")
    W, H = img.size
    draw = ImageDraw.Draw(img)
    titles = []
    if len(title) > 7:
        pieces = title.split()
        titles = (" ".join(pieces[i:i+7]) for i in range(0, len(pieces), 7))
    else:
        titles.append(title)
    
    w = 130
    h = img.height / 2
    for tit in titles:
        draw.text((w,h), tit, fill="black", font=font)
        h += 35
    img.save("temp_thumbnail.png")

def add_thumb(video_path, thumbnail_path, duration):
    video = editor.VideoFileClip(video_path)

    thumbnail = editor.ImageClip(thumbnail_path).set_start(0).set_duration(duration).set_pos(("center","center")).resize(height=350)

    final = editor.CompositeVideoClip([video, thumbnail])
    final.write_videofile("temp_vid_thumb.mp4")

def main():
    create_thumbnail("AITA for something something something something something eight nine ten eleven twelve thirteen")
    add_thumb("temp_vid.mp4", "temp_thumbnail.png", 1)

if __name__ == "__main__":
    main()