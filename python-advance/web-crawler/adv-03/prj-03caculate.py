from tkinter import*

def convert ():
    num=float(data.get())
    num1=data1.get()
    num2=float(data2.get())
    print(num,num1,num2)
    if num1=="+":
        put_data.configure(text=str(num+num2))
    elif num1=="-":
        put_data.configure(text=str(num-num2))
    elif num1=="*":
        put_data.configure(text=str(num*num2))
    elif num1=="/":
        put_data.configure(text=str(num/num2))
    else:
        put_data.configure(text="請重新輸入看看")
windows =Tk()
windows.title('my first gui') 

canvas=Canvas(windows,width=100,height=100)
canvas.pack()
msg=Label(windows,text="請輸入數字1",font=('Arial',12))
msg.pack()
data=Entry(windows,text="")
data.pack()
msg1=Label(windows,text="請輸入運算符號",font=('Arial',12))
msg1.pack()
data1=Entry(windows,text="")
data1.pack()
msg2=Label(windows,text="請輸入數字2",font=('Arial',12))
msg2.pack()
data2=Entry(windows,text="")
data2.pack()
put_data=Label(windows,text="")
put_data.pack()

btn=Button(windows,text="結果",command=convert)
btn.pack()

windows.mainloop()