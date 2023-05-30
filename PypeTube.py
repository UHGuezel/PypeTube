
from pytube import YouTube

PATH_SOURCE = "toDownload.txt"
CONTENT_SOURCE = open(PATH_SOURCE, 'r').readlines()
MAX_LINES = len(CONTENT_SOURCE)

try:
    for count, link in enumerate(CONTENT_SOURCE):
        yt = YouTube(link)
        ys = yt.streams.get_audio_only()
        print(f"Download starts... ({count+1}/{MAX_LINES})")
        ys.download('Downloads')
    print("Download finished!")
except:
    print("Something must be wrong with one or more links...")