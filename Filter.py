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