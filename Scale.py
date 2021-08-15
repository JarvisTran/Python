from tkinter import *

def submit():
    print("The temperature is:"+str(scale.get())+" degree C")

window = Tk()
hotImage = PhotoImage(file = "pizza.gif")
hotLabel = Label(image=hotImage)
hotLabel.pack()

scale = Scale(window,
              from_ = 1000,
              to_ = 0,
              length = 600,
              orient = VERTICAL,
              font = ("Consolas",20),
              tickinterval = 10,
              showvalue = 0,
              resolution = 5,
              throughcolor ="#69EAFF",
              fg = "#FF1C00",
              bg = "#111111",
              )

scale.set(50)
scale.set(((scale['from']-scale["to"])/2) + scale["to"])
scale.pack()

button = Button(window, text="submit", command = submit)
button.pack()

window.mainloop()

