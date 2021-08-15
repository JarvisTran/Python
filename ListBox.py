from tkinter import *
window = Tk()

def submit():
    food =[]
    for index in listbox.curselection():
        food.insert(index, listbox.get(index))
    print("you have ordered: ")
    print(listbox.get(listbox.curselection()))
def add():

    listbox.insert(listbox.size(), entryBox.get())
    listbox.config(heigh=listbox.size())
def delete():
    for index in reversed(listbox.curselection()):
        listbox.delete(index)


    listbox.config(heigh=listbox.size())

listbox = Listbox(window,
                  bg="#f7ffde",
                  font=("Constantia",35),
                  width=12,


                  )
listbox.pack()

listbox.insert(1,"pizza")
listbox.insert(2,"pasta")
listbox.insert(3,"garlic bread")
listbox.insert(4,"soup")

listbox.config(height=listbox.size())

entryBox = Entry(window)
entryBox.pack()

submitButton = Button(window, text="submit", command=submit )
submitButton.pack()

addButton = Button(window, text="add", command=add)
addButton.pack()

deleteAddButton = Button(window, text="delete", command=delete)
deleteAddButton.pack()

window.mainloop()