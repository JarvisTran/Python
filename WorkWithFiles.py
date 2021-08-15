# Write a file

text = "yooooo \nthis is some text \nsee ywah"
with open('test.txt','w') as file:
    file.write(text)

# Copy a file

import shutil
shutil.copyfile("test.txt", "C:\\Users\\ngocc\\PycharmProjects\\pythonProject1\\copy.txt")

# move files

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
