from tkinter import *

from tkinter import messagebox

window = Tk()

window.title("Turtle Code")

window.geometry('350x200')

def clicked():
    messagebox.showwarning("Warning","Warning message")

btn = Button(window,text='Click here', command=clicked)

btn.grid(column=0,row=0)

window.mainloop()