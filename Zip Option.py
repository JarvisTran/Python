usernames = ["Dude", "Bro", "Mister"]
passwords = ("p@ssword", "abcd1234", "guest1023")
login_date = ["1/1/2021","2/7/2021","9/9/2021"]


users = dict(zip(usernames, passwords))
print(type(users))
for key, value in users.items():
    print(key + ": "+value)


users1 = zip(usernames,passwords,login_date)
for i in users1:
    print(i)