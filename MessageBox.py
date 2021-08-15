from tkinter import messagebox
from tkinter import *

def click():
    #messagebox.showinfo(title="this is an info message box",message="you are a person")
    #while True:
    #   messagebox.showwarning(title="WARNING!", message="you have a virus!!!")
    #messagebox.showerror()
    #if messagebox.askokcancel(title="ask ok cancle", message="do you want to do the thing"):
    #    print("You did a thing!")
    #else:
    #    print("You canceled a thing! ")
    #if messagebox.askretrycancel()
    #messagebox.askyesno()
    pass
window = Tk()
button = Button(window, command = click, text="click me")
button.pack()

window.mainloop()