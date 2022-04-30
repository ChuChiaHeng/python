from tkinter import*
def hi_fun():
    display.config(text="what the funk",fg="yellow",bg="pink")
def hi_funk():
    display.config(text="",bg="gray")
windows =Tk()
windows.title('my first gui') 
btn1=Button(windows,text="show screen",command=hi_fun)
btn2=Button(windows,text="clear screen",command=hi_funk)
btn1.pack()
btn2.pack()
display=Label(windows,text="")
display.pack()
windows.mainloop()  