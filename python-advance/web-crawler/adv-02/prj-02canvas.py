from tkinter import*
def move_r(event):
    key=event.keysym
    if key=="Right":
        canvas.move(circle,10,0)
    elif key=="Left":
        canvas.move(circle,-10,0)
    elif key=="Up":
        canvas.move(circle,0,-10)
    elif key=="Down":
        canvas.move(circle,0,10)
    elif key=="d":
        canvas.move(rect,10,0)
    elif key=="a":
        canvas.move(rect,-10,0)
    elif key=="w":
        canvas.move(rect,0,-10)
    elif key=="s":
        canvas.move(rect,0,10)
windows=Tk()
windows.title("my first gui")
canvas=Canvas(windows,width=600,height=600)
canvas.pack()
img=PhotoImage(file="adv-02/crocodile2.gif")
my_img=canvas.create_image(500,500,image=img)
circle=canvas.create_oval(200,200,400,400,fill="red")
rect=canvas.create_rectangle(220,400,380,430,fill="blue")
canvas.bind_all('<Key>',move_r)
msg=canvas.create_text(300,100,text="Crocodile",fill="black",font=('Arial',30))

windows.mainloop()
