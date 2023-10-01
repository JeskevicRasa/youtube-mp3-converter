from pytube import YouTube

url = "https://www.youtube.com/watch?v=eNUpTV9BGac"

try:
    video = YouTube(url)
    stream = video.streams.filter(only_audio=True).first()
    stream.download(filename=f'{video.title}.mp3')
    print('MP3 downloaded')
except KeyError:
    print('Unable to fetch video information. Please check the video URL')
