import os
from pytube import YouTube

PATH_SOURCE = "toDownload.txt"
DEST_PATH = "Downloads"
CONTENT_SOURCE = open(PATH_SOURCE, 'r').readlines()
MAX_LINES = len(CONTENT_SOURCE)

if os.path.exists(DEST_PATH):
    print("Skip creation of Dest-File: File already exists.")
else:
    os.makedirs(DEST_PATH)

try:
    for count, link in enumerate(CONTENT_SOURCE):
        yt = YouTube(link)
        ys = yt.streams.get_audio_only()
        print(f"Download starts... ({count+1}/{MAX_LINES})")
        ys.download('Downloads')
    print("Download finished!")
except:
    print("Something must be wrong with one or more links...")