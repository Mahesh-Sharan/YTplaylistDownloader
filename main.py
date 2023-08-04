from pytube import Playlist, YouTube
from tqdm import tqdm
import os

def download_playlist(url, output_path):
    playlist = Playlist(url)
    total_videos = len(playlist.video_urls)

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    for video_url in tqdm(playlist.video_urls, desc="Downloading Playlist", unit="video"):
        video = YouTube(video_url)
        stream = video.streams.get_highest_resolution()
        stream.download(output_path)

    print("Download complete!")

if __name__ == "__main__":
    playlist_url = input("Enter the YouTube playlist URL: ")
    output_folder = input("Enter the output folder path: ") # eg "(Downloads/GtaV)" ,Downloads is the directory and GtaV is new folder created inside Downloads Directory
    download_playlist(playlist_url, output_folder)
