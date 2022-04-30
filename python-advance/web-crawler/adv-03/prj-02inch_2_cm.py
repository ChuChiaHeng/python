from tkinter import*

def convert ():
    data=inch_data.get()
    print(data)
    if data !="":
        put_str =str(int(data)*2.54)
        put_data.configure(text=put_str)
windows =Tk()
windows.title('my first gui') 

canvas=Canvas(windows,width=100,height=100)
canvas.pack()
msg=Label(windows,text="請輸入英吋",font=('Arial',12))
msg.pack()
inch_data=Entry(windows,text="")
inch_data.pack()
put_data=Label(windows,text="")
put_data.pack()

btn=Button(windows,text="轉換",command=convert)
btn.pack()

windows.mainloop()