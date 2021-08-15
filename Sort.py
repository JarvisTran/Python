students = [("john", "F", 60),
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
    print("\n", i)
