from pytube import YouTube

link =  "https://youtu.be/NLKwRW2y-sg"
video = YouTube(link)


print(".*.*.*.*.*.*.*.*.*.* VIDEO TITLE .*.*.*.*.*.*.*.*.*.*")
print(video.title)


print(".*.*.*.*.*.*.*.*.*.*  DOWNLOAD VIDEO AND AUDIO LINK .*.*.*.*.*.*.*.*.*.*")
video_1 = video.streams.all()    


vid = list(enumerate(video_1))
for i in vid:
    print(i)
print()


button = int(input("Enter the  Video , Audio quality in index number:"))
video_1[button].download()
print("Downloaded Successfully")