from PIL import Image, ImageFont, ImageDraw
from moviepy import editor
from moviepy.video.fx.all import resize

def create_thumbnail(title):
    font = ImageFont.truetype('/Library/Fonts/Inter-Bold.ttf', 30)
    img = Image.open("Template.png")
    W, H = img.size
    draw = ImageDraw.Draw(img)
    w = draw.textlength(title)
    h = 10
    draw.text(((W-w)/2,(H-h)/2), title, fill="black", font=font)
    img.save("thumb_test.png")

def add_thumb(video_path, thumbnail_path, duration):
    video = editor.VideoFileClip(video_path)

    thumbnail = editor.ImageClip(thumbnail_path).set_start(0).set_duration(duration).set_pos(("center","center")).resize(height=75)

    final = editor.CompositeVideoClip([video, thumbnail])
    final.write_videofile("test_3.mp4")

def main():
    return

if __name__ == "__main__":
    main()