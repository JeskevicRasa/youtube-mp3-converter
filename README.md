# YouTube to MP3 Converter

This Python script allows you to convert YouTube videos to MP3 audio files using the Pytube library. It's a simple and straightforward way to extract the audio from a YouTube video and save it as an MP3 file.

## Prerequisites

Before you can use this script, make sure you have the following prerequisites installed:

- Python 3.x
- Pytube library (you can install it using `pip install pytube`)

## Usage

1. Open your Python code editor, such as PyCharm.

2. Paste the following code into a Python script file (e.g., `youtube_to_mp3.py`):

```python
from pytube import YouTube

url = "https://www.youtube.com/watch?v=eNUpTV9BGac"

try:
    video = YouTube(url)
    stream = video.streams.filter(only_audio=True).first()
    stream.download(filename=f'{video.title}.mp3')
    print('MP3 downloaded')
except KeyError:
    print('Unable to fetch video information. Please check the video URL')

```

1. Replace the url variable value with the YouTube video URL that you want to convert to MP3.

2. Save the script.

3. Run the script using Python. You can do this by right-clicking the script file and selecting "Run" in PyCharm or running it from the command line with python youtube_to_mp3.py.

4. The script will download the audio from the provided YouTube video and save it as an MP3 file in the same directory as your script. The filename will be based on the title of the YouTube video.

5. Once the script finishes running, you'll see the message "MP3 downloaded" if the conversion was successful.

## Notes
Ensure that you have a stable internet connection when running the script as it needs to fetch video information from YouTube.

If you encounter any issues or errors, make sure to check the video URL and ensure it's valid.

This script only downloads the audio track in MP3 format. If you need other formats or options, you can explore the Pytube library's documentation for more functionality.

## Disclaimer
Please be aware of copyright and intellectual property rights when using this script to download content from YouTube. Ensure that you have the necessary permissions to download and use the content.

Enjoy using this YouTube to MP3 converter script!