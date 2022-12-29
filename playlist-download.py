from pytube import Playlist


get_user_input_link = input("Enter The Playlist URL:- ")

Youtube_playlist = Playlist(get_user_input_link)

#You can find the location in your file explorer [Example:- (D:\Videos)]

download_location = input("Enter the location where you want to download the videos:- ")

for video in Youtube_playlist.videos:
    video.streams.get_highest_resolution().download(download_location)
    print("Video Downloaded", video.title)

print("Playlist Downloaded")