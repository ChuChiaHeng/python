from tkinter import*
from pytube import YouTube
from moviepy.editor import VideoFileClip
import os
def get_movie ():
    name=name_info.get()
    url=url_info.get()
    url1=url1_info.get()
    chk_val=state.get()

    video_path="adv-13/"+name
    if os.path.isfile(video_path):
        clip=VideoFileClip(video_path)
        clip=clip.subclip(url,url1)
    else:
        exit()
    base_path="adv-13/"
    new_file="uber-cut"
    new_path=base_path+new_file+".mp4"
    i=0
    while os.path.isfile(new_path):
        i+=1
        new_path=base_path+new_file+str(i)+".mp4"
    print(new_path)
    clip.write_videofile(new_path)
    if chk_val==True:
        new_path=base_path+new_file+str(i)+".gif"
        clip.write_gif(new_path)
    movie_name.config(text="切割完成")
    
windows = Tk()
windows.title("My Gif")
url = Label(windows, text="請輸入開始時間", font=('Arial', 12))
url.grid(row=0, column=0)
url_info = Entry(windows)
url_info.grid(row=0, column=1)
url1 = Label(windows, text="請輸入結束時間", font=('Arial', 12))
url1.grid(row=1, column=0)
url1_info = Entry(windows)
url1_info.grid(row=1, column=1)
name = Label(windows, text="請輸入影片名稱", font=('Arial', 12))
name.grid(row=2, column=0)
name_info = Entry(windows)
name_info.grid(row=2, column=1)
state=BooleanVar()
state.set(True)
chk=Checkbutton(windows,text="gif",var=state)
chk.grid(row=3,column=0)
btn = Button(windows, text='開始分割', command=get_movie)
btn.grid(row=3, columnspan=2)
movie_name = Label(windows, text="")
movie_name.grid(row=4, columnspan=2)
windows.geometry("300x150")
windows.mainloop()