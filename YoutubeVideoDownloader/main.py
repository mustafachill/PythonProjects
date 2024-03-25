import pytube

url = input("enter url which you want to download from youtube: ")
path = ""
pytube.YouTube(url).streams.get_highest_resolution().download(path)
