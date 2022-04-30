from tkinter import*

def hi_fun ():
    print("hello hhhaaa")
    display.config(text="hi singular",fg="yellow",bg="brown")


windows =Tk()
windows.title('my first gui') 

btn=Button(windows,text="click me",command=hi_fun)
btn.pack()
display=Label(windows,text="")
display.pack()

windows.mainloop()  

