from pytube import YouTube
from moviepy.editor import VideoFileClip
import os
yt=YouTube("https://www.youtube.com/watch?v=HpxnAkGBdSY")
print("We are downloading video...")
video=yt.streams
result=video.filter(progressive=True,subtype="mp4",res="360p")
print(result[0])
dest="adv-13/"
fname=("uber.mp4")
result[0].download(output_path=dest,filename=fname)
print("Download finished...")
video_path="adv-13/uber.mp4"
if os.path.isfile(video_path):
    clip=VideoFileClip(video_path)
    clip=clip.subclip(8,14)
else:
    exit()
base_path="adv-13/"
new_file="uber-cut"
new_path=base_path+new_file+".gif"
i=0
while os.path.isfile(new_path):
    i+=1
    new_path=base_path+new_file+str(i)+".gif"
print(new_path)
clip.write_gif(new_path)