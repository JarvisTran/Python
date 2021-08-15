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