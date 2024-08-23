from tiktok_uploader.upload import upload_video
from tiktok_uploader.auth import AuthBackend

def schedule_and_upload_videos():
	auth = AuthBackend(cookies='Upload/cookies.txt')
	upload_video(filename='tiktoks/tiktok_1.mp4', description='#fyp #AITA #Reddit #Minecraft', auth=auth)

def main():
	schedule_and_upload_videos()

if __name__ == '__main__':
	main()