from tkinter import *
a=0
def get_cut(a):
    rad_val=sel.get()
    
    a+=rad_val
    print(a)
windows=Tk()
windows.title("My Video")
sel=IntVar()
sel.set(-1)
rad=Radiobutton(windows,text="mp4",value=0,var=sel,command=get_cut(a))
rad.grid(row=0,column=0)
rad1=Radiobutton(windows,text="gif",value=3,var=sel,command=get_cut(a))
rad1.grid(row=0,column=1)
rad2=Radiobutton(windows,text="mp3",value=5,var=sel,command=get_cut(a))
rad2.grid(row=0,column=2)

windows.geometry("150x50")
windows.mainloop()