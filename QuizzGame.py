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