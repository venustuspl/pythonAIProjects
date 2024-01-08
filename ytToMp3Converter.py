from pytube import YouTube
from moviepy.editor import *

# Pobranie wideo z <link>YouTube</link>
url = "https://www.youtube.com/watch?v=pArRaiGE5dI"
yt = YouTube(url)
video = yt.streams.filter(only_audio=True).first()
video.download(filename="video")

# Konwersja do formatu mp3
video = VideoFileClip(video)
video.audio.write_audiofile("audio.mp3")

# Usunięcie pliku wideo
os.remove("video.mp4")