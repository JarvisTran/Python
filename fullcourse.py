# String Slicing
'''
website1 = "http://google.com"
website2 = "http://wikipedia.com"

slice = slice(7,-4)

print(website1[slice])
print(website2[slice]) '''

# While loop
import shutil
import tkinter

'''
name = ''
while len(name) == 0:
    name = input('enter your name: ')
print("hello " + name)'''

# For loop
'''
import time

for seconds in range (10,0,-1):
    print(seconds)
    time.sleep(1)
print("happy new year")
'''

# Nested loops
'''
rows = int(input("How many rows?: "))
columns = int(input("How many columns: "))
symbols = input("Enter a symbol to use: ")

for i in range(rows):
    for j in range(columns):
        print(symbols, end="")  #without end, its gonna move to the nexr line due to print command
    print()  #move to the next line
'''

'''
phone_numbers = '123-456-789'
for i in phone_numbers:
    if i == '-':
        continue
    print(i, end='')
    '''

'''
for i in range (24):
    if i == 13:
        pass
    else:
        print(i)
'''

# Recursion
'''
def fib(n):

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return

print(fib(1))
print(fib(5))
print(fib(6))
print(fib(7))'''

'''sum1 = 0
a = int(input('enter n: '))
for i in range(1, a+1):
    sum1 += i**3
print(sum1)

print(sum([i**3 for i in range(1, int(input())+1)]))'''

'''
def recursion(n):
    if n == 1:
        return 1
    return recursion(n-1) + n**3

print(recursion(3))

'''

# Write a file

'''text = "yooooo \nthis is some text \nsee ywah"
with open('test.txt','w') as file:
    file.write(text)'''

# Copy a file

'''import shutil
shutil.copyfile("test.txt", "C:\\Users\\ngocc\\PycharmProjects\\pythonProject1\\copy.txt")'''

# move files
'''
import os
import shutil

source = "folder"
destination = "C:\\Users\\ngocc\\Desktop\\folder"

try:
    if os.path.exists(destination):
        print("there is already a file there")
    else:
        os.replace(source, destination)
        print(source+" was moved")
except:
    print(source+"was not found")

#os.remove()                  #Delete a file
#os.rmdir("test1")            #Delete an empty directory
#shutil.rmtree()              #Delete a directory containing files

'''

# rock, paper, scissors game

'''
import random

while True:

    choices = ("scissors", "rock", "paper")

    computer = random.choice(choices)
    player = None


    while player not in choices:
        player = input("scissors, rock, paper: ").lower()

    if computer == player:
        print("computer", computer)
        print("player", player)
        print("tie")
    elif player == "rock":
        if computer == "scissors":
            print("computer", computer)
            print("player", player)
            print("player win")
        elif computer == "paper":
            print("computer", computer)
            print("player", player)
            print("computer win")
    elif player == "scissors":
        if computer == "rock":
            print("computer", computer)
            print("player", player)
            print("computer win")
        elif computer == "paper":
            print("computer", computer)
            print("player", player)
            print("player win")
    elif player == "paper":
        if computer == "scissors":
            print("computer", computer)
            print("player", player)
            print("computer win")
        elif computer == "rock":
            print("computer", computer)
            print("player", player)
            print("player win")
    play_again = input("want to play again? Yes/No ").lower()
    if play_again != "yes":
        break

print("bye")

'''

# Quizz Game
'''
def new_game():
    question_num = 1
    my_guesses = []
    correct_guesses = 0
    for key in questions:
        print("-----------------------------")
        print(key)
        for j in options[question_num-1]:
            print(j)
        my_answer = input("Your answer (A, B, C or D): ").upper()
        my_guesses.append(my_answer)
        correct_guesses += check_answers(my_answer, questions.get(key))
        question_num += 1 
    display_score(correct_guesses, my_guesses)


def check_answers(answer, key):
    if answer == key:
        print("correct!")
        return 1

    else:
        print("incorrect")
        return 0


def display_score(correct_answer, answer):
    print("---------------")
    print("RESULTS")
    print("---------------")
    print("Your answers are: ", end="")
    for i in answer:
         print(str(i), end="")
    print("\n---------------")
    print("The correct answer are: ",end ="")
    count = 0
    for i in questions:
        print(questions.get(i), end=" ")
        count += 1
    print("\nScore: " + str(correct_answer) + "/" + str(count))


def play_again():
    play_more = input("Do you want to play again?? (Yes or No) ").upper()
    if play_more == "YES":
        return True
    elif play_more =="No":
        return False
    else:
        print("ByeBye")


questions = {
    "1. Who created python?: ": "A",
    "2. What year was python created?: ": "B",
    "3. Python is tributed to which comedy group": "C",
    "4. Is the Earth round": "A"
}

options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerber"],
           ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
           ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
           ["A. True", "B. False"]
]

new_game()
while play_again():
    new_game()

'''

# Object oriented Programming

'''from car import Car
print(Car("as", "as", "as", "as"))

car_1 = Car("Chevy", "Corvette", 2021, "Blue")
car_2 = Car("Honda", "Accord", 2011, "Black")
print(car_1.make)
print(car_1.model)
print(car_1.year)
car_1.drive()
car_1.stop()


print(car_1.wheels)'''

'''
def recursion_1(n):
    for i in range(n):
        print("*", end="")
        if i == n-1:
            print(" ")
    recursion_1(n-2)
recursion_1(10)

'''

# super function
'''
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

class Square(Rectangle):
    def __init__(self, length, width):
        super().__init__(length, width)
    def Area(self):
        return self.length*self.width


class Cube(Rectangle):
    def __init__(self, length, width, height):
        self.height = height
        super().__init__(length, width)
    def Volume(self):
        return self.height*self.width*self.length


square = Square(3,3)
cube = Cube(3,3,3)

print(square.Area())
print(cube.Volume())

'''

# Abstracts class
'''
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

class Car(Vehicle):
    def go(self):
        print("you drive the car")

class Motorcycle(Vehicle):
    def go(self):
        print("you ride the motorcycle")

vehicle = Vehicle()
vehicle.go()
car = Car()
car.go()

'''

# Object as argument
'''
class Car:
    color = None

class Motorcycle:
    pass


def change_color(vehicle, color):
    vehicle.color = color

car1 = Car()
change_color(car1, "red")
print(car1.color)
'''

# Duck typing
''''
class Duck:
    def walk(self):
        print("this duck is walking")
    def talk(self):
        print("this duck is qwacking")
class Chicken:
    def walk(self):
        print("this chicken is walking")
    def talk(self):
        print("this chicken is clucking")

class Person():
    def catch(self, duck):
        duck.walk()
        duck.talk()
        print("you caught the critter")


duck = Duck()
chicken = Chicken()
person = Person()

person.catch(chicken)
person.catch(duck)
'''

# Walrus operator

# 1
'''print(happy := True)
foods = list()
while True:
    food = input("what food do you like?: ")
    if food == "quit":
        break
    foods.append(food)
print(foods)'''
# 2
'''foods1 = list()
while food1 := input("what food do you like?: ") != "quit":
    foods1.append(food1)
print(foods1)'''

# Higher order function

# 1
'''
def loud(text):
    return text.upper()

def quite(text):
    return text.lower()
def hello(func):
    text = func("Hello")
    print(text)

hello(loud)
hello(quite)
'''

# 2
'''
def divisor(x):
    def dividend(y):
        return y/x
    return dividend

devide = divisor(2)
print(devide(10))'''

# LAMBDA

'''age_check = lambda age: True if age >= 18 else False
print(age_check(20))
'''

'''
class Solution:
    def lexicalOrder(self, n: int):
        result = []
        current = 0  # Start with 0
        for i in range(n):
            last_digit = current % 10
            down = current * 10
            if down == 0:  # Special case - first step
                down = 1
            if down <= n:
                current = down
            elif last_digit < 9 and current+1 <= n:
                current += 1
            else:
                up = current // 10
                while up % 10 == 9:
                    up //= 10
                current = up+1
            result.append(current)
        return result

solu1 = Solution()
print(solu1.lexicalOrder(32))
'''
# print(11%10)


'''
class Solution:
    def addTwonumber(self, l1: [int], l2: [int]):
        l3 = []
        l5 = []
        for i in l1:
            l1 += str(i)
        for j in l2:
            l2 += str(j)
        k = int(l1)+int(l2)
        h = str(k)
        for ch in h:
            l3.append(ch)
        l4 = reversed(l3)
        for reverse in l4:
            l5.append(reverse)
        return l5
solu = Solution()
print(solu.addTwonumber([2,3,4],[5,6,7]))
'''

# 1
'''class solution:
    def twoSum(self,nums: [int], target: int):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == target - nums[j]:
                    return [i, j]'''
# 2
'''class Solution:
    def twoSum(self, nums: [int], target: int):
        hashmap ={}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
            print(hashmap)
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i :
                return [i, hashmap[complement]]
solu = Solution()
print(solu.twoSum([2,3,6,4,7,8,9,5],9))
'''

# Sort

'''students = [("john", "F", 60),
            ("Sandy","A",33),
            ("Patrick","D", 36),
            ("Spongenbob","B",20)
            ]
grade = lambda grades: grades[1]
students.sort(key=grade, reverse=True)
for i in students:
    print(i)
age = lambda ages: ages[2]
students.sort(key=age)
for i in students:
    print("\n", i)'''

# Map
'''
store = [
    ("shirt", 20.00),
    ("pants", 25.00),
    ("jacket", 50.00),
    ("socks", 10.00)
]

to_euros = lambda data: (data[0], data[1]*0.82)
to_dollars = lambda data: (data[0], data[1]/0.82)
store_euros = list(map(to_euros, store))
store_dollars = list(map(to_dollars, store))
for i in store_euros:
    print(i)
for i in store_dollars:
    print(i)'''

# Filter
'''
friends = [("Rachel",19),
           ("Monica", 18),
           ("Phoebe", 17),
           ("Joey",16),
           ("Chandler",21),
           ("Ross", 20)
           ]

age = lambda ages: ages[1]>=18
drinking_buddies = list(filter(age, friends))
for i in drinking_buddies:
    print(i)
'''

# REDUCE
'''
import functools

letter = ["H", "E", "L", "L", "O"]
word = functools.reduce(lambda x, y: x + y, letter)
print(word)

factorial = [5, 4, 3, 2, 1]
result = functools.reduce(lambda x, y: x * y, factorial)
print(result)
'''


#LIST COMPREHENSION
'''
square = [i * i for i in range(1,11)]
print(square)

students = [100,90,87,84,24,56,48,90]

pass_students = list(filter(lambda x: x >= 60, students))
print(pass_students)

pass_students2 = [i for i in students if i >= 60]
print(pass_students2)

pass_student3 = [i if i>= 60 else "False" for i in students]
print(pass_student3)

'''


#Dictionary comprehension

'''cities_in_F = {"New York": 32, "Boston":75, "Los Angeles":100, "Chicago":50}

cities_in_C = {key: round((value-32)*(5/9)) for (key,value) in cities_in_F.items()}
print(cities_in_C)
for i in cities_in_F.keys():
    print(i)
print(cities_in_F.values())
print(cities_in_F.items())'''


#IF
'''weather = {"New York":"snowing","Boston":"sunny","Los Angeles":"sunny","Chicago":"cloudy"}

sunny_weather = {key: value for (key, value) in weather.items() if value == "sunny"}
print(sunny_weather)


'''
#IF ELSE
'''cities = {"New York": 32, "Boston": 75, "Los Angeles": 100, "Chicago": 50}
desc_weather = {key: "WARM" if value >= 50 else "Cold" for (key,value) in cities.items()}
print(desc_weather)
'''
#Function
'''def check_temp(value):
    if value >=70:
        return "HOT"
    elif 69 >= value >= 40:
        return "WARM"
    else:
        return "COLD"

cities = {"New York": 32, "Boston": 75, "Los Angeles": 100, "Chicago": 50}
desc_weather = {key: check_temp(value) for (key,value) in cities.items()}
print(desc_weather)'''


#ZIP OPTION
'''usernames = ["Dude", "Bro", "Mister"]
passwords = ("p@ssword", "abcd1234", "guest1023")
login_date = ["1/1/2021","2/7/2021","9/9/2021"]


users = dict(zip(usernames, passwords))
print(type(users))
for key, value in users.items():
    print(key + ": "+value)


users1 = zip(usernames,passwords,login_date)
for i in users1:
    print(i)'''






#if __name__ == "__main__":
'''
import time
print(time.ctime(time.time()))
print("")
time_object = time.localtime()
print(time_object)
print("")
print(time.strftime("%a %B %Y %H:%M:%S", time_object))
print("")


#time_string = "20 April, 2020"
#time_object1 = time.strptime(time_string, "%d %B %Y")
#print(time_object1)


time_tupple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
time_string = time.asctime(time_tupple)
print(time_string)


time_tupple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
time_string = time.mktime(time_tupple)
print("\n", time_string)

'''


#THREADIG
'''import threading
import time

def eat_breakfast():
    time.sleep(3)
    print("you eat breakfast")

def drink_coffee():
    time.sleep(4)
    print("you drink coffe")

def study():
    time.sleep(5)
    print("you finish studying")

x= threading.Thread(target = eat_breakfast, args=())
x.start()

y = threading.Thread(target=drink_coffee(),args =())
y.start()

z = threading.Thread(target=study(), args=())
z.start()

x.join()
y.join()
z.join()

print(threading.activeCount())
print(threading.enumerate())
print(time.perf_counter())'''


#DAEMON THREAD

'''import threading
import time

def timer():
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("logged in for: ",count," seconds")

x = threading.Thread(target=timer(), daemon=True)
x.start()

answer = input("Do you wish to exit?")
'''

#MULTI-PROCESSING

'''
from multiprocessing import Process, cpu_count
import time

def counter(num):
    count = 0
    while count < num:
        count += 1

def main():

    a = Process(target=counter, args=(125000000,))
    b = Process(target=counter, args=(125000000,))
    c = Process(target=counter, args=(125000000,))
    d = Process(target=counter, args=(125000000,))
    e = Process(target=counter, args=(125000000,))
    f = Process(target=counter, args=(125000000,))
    g = Process(target=counter, args=(125000000,))
    h = Process(target=counter, args=(125000000,))

    a.start()
    b.start()
    c.start()
    d.start()
    e.start()
    f.start()
    g.start()
    h.start()


    a.join()
    b.join()
    c.join()
    d.join()
    e.join()
    f.join()
    g.join()
    h.join()

    print("finish in:",time.perf_counter(),"seconds")

if __name__ == '__main__':
    main()

'''
#GUI WINDOW
'''
from tkinter import *

print(tkinter.TkVersion)
window = Tk()
window.geometry("420x420")
window.title("First design")

icon = PhotoImage(file = "download1.gif")
window.iconphoto(True, icon)
window.config(background = "#3474eb")

window.mainloop()'''

#LABEL

'''from tkinter import *
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
window.mainloop()'''


#Buttons
'''
from tkinter import *

count = 0
def click():

    global count
    count += 1
    print(count)
window = Tk()

photo = PhotoImage(file="download1.gif")

button = Button(window,
                text = "click me!",
                command = click,
                font= ("Comic Sans", 30),
                fg = "#00FF00",
                bg = "black",
                activeforeground = "#00FF00",
                activebackground = "black",
                image = photo,
                compound = "top"
                )

button.pack()

window.mainloop()'''


#ENTRY BOX
'''
from tkinter import *

def submit():
    username = entry.get()
    print("Hello: "+username)
    #entry.config(state= DISABLED)
def delete():
    entry.delete(0, END)

def backspace():
    entry.delete(len(entry.get())-1, END)

window = Tk()
entry = Entry(window,
            font= ("Arial", 50),
            fg= "#00FF00",
            bg= "black",
            show="*"
              )

#entry.insert(0,"HELLU")
entry.pack(side= LEFT)

submit_button = Button(window, text = "submit", command = submit)
submit_button.pack(side = RIGHT)

delete_button = Button(window, text = "delete", command = delete)
delete_button.pack(side = RIGHT)

backspace_button = Button(window, text = "backspace", command = backspace)
backspace_button.pack(side = RIGHT)

window.mainloop()
'''


#CHECKBOX
'''
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
'''



#RADIO BUTTON
'''
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
'''




#SCALE
'''
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
              throughcolor = "#69EAFF",
              fg = "#FF1C00",
              bg = "#111111",
              )

scale.set(50)
scale.set(((scale['from']-scale["to"])/2) + scale["to"])
scale.pack()

button = Button(window, text="submit", command = submit)
button.pack()

window.mainloop()
'''


#LISTBOX
'''
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
'''



#MESSAGE BOX

'''from tkinter import messagebox
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
'''


#ColorChooser
'''
from tkinter import *
from tkinter import colorchooser

def click():
    color = colorchooser.askcolor()
    window.config(bg=color[1])
 

window = Tk()
window.geometry("420x420")
button = Button(text = "click me", command = click)
button.pack()
window.mainloop()

'''

#TEXT AREA

'''from tkinter import *

def submit():
    input = text.get("1.0",END)
    print(input)

window = Tk()
text = Text(window,
            bg= "#fb464a",
            font = ("Ink Free",25),
            height = 8,
            width = 20,
            padx = 20,
            pady = 20,
            )
text.pack()
button = Button(window, text="submit", command = submit)
button.pack()
window.mainloop()
'''



#Open a file

'''from tkinter import *
from tkinter import filedialog

def openFile():
    filepath = filedialog.askopenfilename(initialdir = "C:\\Users\\ngocc\\PycharmProjects\\PythonProjects",
                                          title="Opening file",
                                          filetypes = (("text file","*.txt"),("all files","*.*")
                                          ))
    file = open(filepath, "r")
    print(file.read())
    file.close()

window = Tk()
button = Button(text= "Open", command = openFile)
button.pack()
window.mainloop()'''



#SAVE FILE


from tkinter import *
from tkinter import filedialog

def saveFile():
    file = filedialog.asksaveasfilename(defaultextension = ".txt",
                                        filetypes = [
                                            ("Text file",".txt"),
                                            ("HTML file",".html"),
                                            ("All files",".*")
                                        ]
                                        )
    file_text = str(text.get(1.0, END))
    file.write(file_text)
    file.close()

window = Tk()
button = Button(text = "save", command = saveFile)
button.pack()
text = Text(window)
text.pack()
window.mainloop()















