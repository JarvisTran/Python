from tkinter import *


window = Tk()
window.geometry("420x420")
window.title("First design")

icon = PhotoImage(file = "download1.gif")
window.iconphoto(True, icon)
window.config(background = "#3474eb")

window.mainloop()