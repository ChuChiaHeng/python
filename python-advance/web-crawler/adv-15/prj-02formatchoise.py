from tkinter import*
from pytube import YouTube
from moviepy.editor import VideoFileClip
import os

def get_movie ():
    chk=sel.get()
    name=name_info.get()
    video_path="adv-14/"+name

    if chk==5:
        url=url_info.get()
        url1=url1_info.get()
        video_path="adv-14/"+name+".mp4"
        if os.path.isfile(video_path):
            clip=VideoFileClip(video_path)
            clip=clip.subclip(url,url1)
        else:
            exit()
        base_path="adv-15/"
        new_file=name+"-cut"
        new_path=base_path+new_file+".mp3"
        i=0
        while os.path.isfile(new_path):
            i+=1
            new_path=base_path+new_file+str(i)+".mp3"
        print(new_path)
        clip.audio.write_audiofile(new_path)

    elif chk==0:
        url=url_info.get()
        url1=url1_info.get()
        video_path="adv-14/"+name+".mp4"
        if os.path.isfile(video_path):
            clip=VideoFileClip(video_path)
            clip=clip.subclip(url,url1)
        else:
            exit()
        base_path="adv-15/"
        new_file=name+"-cut"
        new_path=base_path+new_file+".mp4"
        i=0
        while os.path.isfile(new_path):
            i+=1
            new_path=base_path+new_file+str(i)+".mp4"
        print(new_path)
        clip.write_videofile(new_path)

    elif chk==3:
        url=url_info.get()
        url1=url1_info.get()
        video_path="adv-14/"+name+".mp4"
        if os.path.isfile(video_path):
            clip=VideoFileClip(video_path)
            clip=clip.subclip(url,url1)
        else:
            exit()
        base_path="adv-15/"
        new_file=name+"-cut"
        new_path=base_path+new_file+".gif"
        i=0
        while os.path.isfile(new_path):
            i+=1
            new_path=base_path+new_file+str(i)+".gif"
        print(new_path)
        clip.write_gif(new_path)

    movie_name.config(text="切割完成")

windows = Tk()
windows.title("My Gif")

url = Label(windows, text="請輸入開始時間", font=('Arial', 12))
url.grid(row=0,column=0)
url_info = Entry(windows)
url_info.grid(row=0,column=1)
url1 = Label(windows, text="請輸入結束時間", font=('Arial', 12))
url1.grid(row=1,column=0)
url1_info = Entry(windows)
url1_info.grid(row=1,column=1)

name = Label(windows, text="請輸入影片名稱", font=('Arial', 12))
name.grid(row=2, column=0)
name_info = Entry(windows)
name_info.grid(row=2, column=1)

sel=IntVar()
sel.set(3)

rad=Radiobutton(windows,text="mp4",value=0,var=sel)
rad.grid(row=4,column=0)
rad1=Radiobutton(windows,text="gif",value=3,var=sel)
rad1.grid(row=4,column=1)
rad2=Radiobutton(windows,text="mp3",value=5,var=sel)
rad2.grid(row=4,column=2)

btn = Button(windows, text='開始分割', command=get_movie)
btn.grid(row=3, columnspan=2)

movie_name = Label(windows, text="")
movie_name.grid(row=5, columnspan=2)

windows.geometry("300x150")
windows.mainloop()