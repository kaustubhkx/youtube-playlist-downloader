from pytube import Playlist


get_user_input_link = input("Enter The Playlist URL:- ")

Youtube_playlist = Playlist(get_user_input_link)

for video in Youtube_playlist.videos:
    video.streams.get_highest_resolution().download("D:\Videos\Javascript-2.0")
    print("Video Downloaded", video.title)

print("Playlist Downloaded")