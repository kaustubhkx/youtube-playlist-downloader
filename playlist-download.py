from pytube import Playlist

get_user_input_link = input("Enter The Playlist URL:- ")

Youtube_playlist = Playlist(get_user_input_link)

download_location = str(input("Enter the location where you want to download the videos:- "))

resolution = input("Resolution:- Press 1 for Low Resolution and 2 for High Resolution:- ")

#You can find the location in your file explorer [Example:- (D:\Videos)]

if resolution==1:
    for video in Youtube_playlist.videos:
        video.streams.get_highest_resolution().download(download_location)
        print("Video Downloaded", video.title)
else:
    for video in Youtube_playlist.videos:
        video.streams.get_lowest_resolution().download(download_location)
        print("Video Downloaded", video.title)

print("Playlist Downloaded")