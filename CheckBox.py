from tkinter import *

def display():
    if (x.get()):
        print("you agree:")
    else:
        print("you dont agree")

window = Tk()

x = BooleanVar()

python_photo = PhotoImage(file="download1.gif")

check_button = Checkbutton(window,
                           text = "I agree to something",
                           variable=x,
                           onvalue=True,
                           offvalue=False,
                           command=display,
                           font= ("Arial",20),
                           fg = "#00FF00",
                           bg="black",
                           activeforeground="#eb5e34",
                           activebackground= "Yellow",
                           padx=25,
                           pady=25,
                           image= python_photo,
                           compound= "left"
)

check_button.pack()
window.mainloop()