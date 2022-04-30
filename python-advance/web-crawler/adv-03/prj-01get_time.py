from tkinter import*
import datetime
def get_date():
    time=datetime.date.today()
    put_data.configure(text=time,fg='red')
def get_time():
    time=datetime.datetime.now().time()
    put_data.configure(text=time,fg='brown')
windows =Tk()
windows.title('my first gui') 

canvas=Canvas(windows,width=100,height=100)
canvas.pack()
put_data=Label(windows,text="")
put_data.pack()

btn=Button(windows,text="時間",command=get_time)
btn.pack()
btn1=Button(windows,text="日期",command=get_date)
btn1.pack()




windows.mainloop()