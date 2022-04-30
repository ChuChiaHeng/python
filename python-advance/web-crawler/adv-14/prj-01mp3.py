from pytube import YouTube
from moviepy.editor import VideoFileClip
import os
yt=YouTube("https://youtu.be/ZsbaD7-4bgc")
print("We are downloading video...")
video=yt.streams
result=video.filter(progressive=True,subtype="mp4",res="360p")
print(result[0])
dest="adv-14/"
fname=("裹著心的光.mp4")
result[0].download(output_path=dest,filename=fname)
print("Download finished...")
video_path="adv-14/裹著心的光.mp4"
if os.path.isfile(video_path):
    clip=VideoFileClip(video_path)
    #clip=clip.subclip(,)
else:
    exit()
base_path="adv-14/"
new_file="裹著心的光"
new_path=base_path+new_file+".mp3"
i=0
while os.path.isfile(new_path):
    i+=1
    new_path=base_path+new_file+str(i)+".mp3"
print(new_path)
clip.audio.write_audiofile(new_path)