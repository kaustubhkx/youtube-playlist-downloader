from pathlib import Path
from tkinter import *
from pytube import Playlist

app = Tk()

app.title("YouTube Video Downloader")
app.geometry("750x400")

Header = Label(text="YouTube Playlist Downloader",font="ariel", pady=20)
Header.pack()

enter_url = Label(text="Enter the YouTube Playlist URL")
enter_url.pack()

entry_url = Entry(width=50)
entry_url.pack()


def download():
    process_downlaoding = Label(text="Downloading...")
    process_downlaoding.pack()
    fetch = str(entry_url.get())
    youtube_video = Playlist(fetch)
    path_download = str(Path.home() / "Downloads")
    for video in youtube_video.videos:
        video.streams.get_highest_resolution().download(path_download)
        title = video.title
        title_label = Label(text=title)
        title_label.pack()

def clear():
    entry_url.delete(0, END)

        
download_button = Button(text="Download", command=download)
download_button.pack()

clear_button = Button(text="Clear",command=clear)
clear_button.pack()




app.mainloop()
