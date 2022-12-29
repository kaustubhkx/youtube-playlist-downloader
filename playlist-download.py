#Make sure the YouTube Playlist is set to Public or Unlisted

from pytube import Playlist

get_user_input_link = input("Enter The Playlist URL:- ")

Youtube_playlist = Playlist(get_user_input_link)

download_location = str(input("Enter the location where you want to download the videos:- "))

video_resolution = int(input("Resolution:- Press 1 for High Resolution and Press 2 for Low Resolution:- "))

#You can find the location in your file explorer [Example:- (D:\Videos)]

if video_resolution==1:
    for video in Youtube_playlist.videos:
        print("Playlist Downloading...")
        video.streams.get_highest_resolution().download(download_location)
        print("Video Downloaded", video.title)
        print("Your Playlist has been downloaded")
elif video_resolution==2:
    for video in Youtube_playlist.videos:
        print("Playlist Downloading...")
        video.streams.get_lowest_resolution().download(download_location)
        print("Video Downloaded", video.title)
        print("Your Playlist has been downloaded")
else:
    print("The Playlist was not downloaded try again!")


