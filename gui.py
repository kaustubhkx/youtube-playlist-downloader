from tkinter import *
from pytube import Playlist
from tkinter import filedialog
import time
import threading

app = Tk()

app.title("YouTube Video Downloader")
app.geometry("750x400")
app.iconphoto(True, PhotoImage(file="images/video-library.png"))

Header = Label(text="YouTube Playlist Downloader",font="ariel", pady=20)
Header.pack()

enter_url = Label(text="Enter the YouTube Playlist URL")
enter_url.pack()

entry_url = Entry(width=50)
entry_url.pack()

def download():
    global downloaded_label,check_path
    time.sleep(1)
    processing_label = Label(text="Processing...")
    processing_label.pack()
    fetch = str(entry_url.get())
    youtube_video = Playlist(fetch)
    processing_label.destroy()
    file = filedialog.askdirectory()
    for video in youtube_video.videos:
        process_downloading = Label(text="Downloading...")
        process_downloading.pack()
        video.streams.get_highest_resolution().download(file)
        process_downloading.destroy()
    downloaded_label = Label(text="Playlist Downloaded")
    downloaded_label.pack()
    path_checker = "Check Folder " + file
    check_path = Label(text=path_checker)
    check_path.pack()   
    print("Done")

def clear():
    entry_url.delete(0, END)
    downloaded_label.destroy()
    check_path.destroy()

download_button = Button(text="Download", command=threading.Thread(target=download).start)
download_button.pack()

clear_button = Button(text="Clear",command=clear)
clear_button.pack()


app.mainloop()
