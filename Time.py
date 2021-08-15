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