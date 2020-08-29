import pytube
video_url = input("Enter URL:") # copy and paste url
youtube = pytube.YouTube(video_url)
video = youtube.streams.first()
video.download('path/to/download')
printf("Done Downloading")
