from pytube import YouTube

while(True):

    link = input("\nLink: ")
    yt = YouTube(link)

    video = yt.streams.get_highest_resolution()
    video.download()
    print("Done!")

    answer = input("Do you want to download another video? (y/n) ")
    if answer == "y":
        continue
    else:
        break

