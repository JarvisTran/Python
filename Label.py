from tkinter import *
window = Tk()
photo = PhotoImage(file ="download1.gif")

label = Label(window,
              text="Hello World",
              font= ("Arial", 40,"bold"),
              fg="#e534eb",
              bg = "black",
              relief = RAISED,
              bd = 10,
              padx = 20,
              pady = 20,
              image = photo,
              compound = "bottom"
              )
label.pack()
#label.place(x=0, y=0)
window.mainloop()