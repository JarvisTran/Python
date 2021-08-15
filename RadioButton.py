from tkinter import *

food=["pizza", "hotdog","hamburger"]

def Order():
    if(x.get()==0):
        print("You ordered pizza!")
    elif (x.get()==1):
        print("You ordered hotdog! ")
    elif (x.get()==2):
        print("You ordered Hamburger!")
    else:
        print("what would you like to order??")

window = Tk()
pizzaImage = PhotoImage(file= "pizza.gif")
hotdogImage = PhotoImage(file="hotdog1.gif")
hamburImage = PhotoImage(file="hambur.gif")

foodImages = [pizzaImage,hotdogImage,hamburImage]
x = IntVar()

for index in range(len(food)):
    radiobutton = Radiobutton(window,
                              text = food[index], #adds text to radio button
                              variable=x, #groups radiobuttons together if they share the same variable
                              value=index, #assigns each radiobutton a different value
                              padx = 25,
                              font=("impact",25),
                              image = foodImages[index],
                              compound = "left",
                              indicatoron = 0, #eliminate circle indicators
                              width = 400, #sets width of radiotbutton
                              command = Order
                              )

    radiobutton.pack(anchor=W)

window.mainloop()