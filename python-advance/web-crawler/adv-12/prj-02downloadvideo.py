from pytube import YouTube
from moviepy.editor import VideoFileClip
yt=YouTube("https://www.youtube.com/watch?v=JwjBbWQs71k")
print("We are downloading video...")
video=yt.streams
result=video.filter(progressive=True,subtype="mp4",res="360p")
print(result[0])
dest="adv-12/"
fname="偉大的渺小.mp4"
result[0].download(output_path=dest,filename=fname)
print("Download finished...")
clip=VideoFileClip(dest+fname)
clip.preview(fps=30)