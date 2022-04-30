from tkinter import *

def show_info():
    chk=state.get()
    if (chk):
        box_label.grid(sticky="w")
        box_entry.grid(sticky="w")
        print('jfjfjf')
    else:
        box_label.grid_forget()
        box_entry.grid_forget()
        print("jfjfjfjfj")
        
windows=Tk()
windows.title("My gui")
box_label=Label(windows, text="label info")
box_entry=Entry(windows)
state=BooleanVar()
state.set(False)
box=Checkbutton(windows, text="show info", var=state, command=show_info)
box.grid(sticky="w")
windows.geometry("300x150")
windows.mainloop()