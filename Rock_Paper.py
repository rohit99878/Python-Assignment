import random


print("Welcome to RPS")

user_score = 0
comp_score = 0
ties = 0

name = input("Enter your name here: ")
print("""
1. Paper vs Rock -> Paper
2. Rock vs Scissor -> Rock
3. Scissors vs Paper -> Scissors
""")
while True:
    choice = int(input("enter your choice 1-Rock, 2-Paper, 3-Scissors: "))
    while choice > 3 or choice < 1:
        choice = int(input("enter valid input: "))

    if choice == 1:
        user_choice = "Rock"
    elif choice == 2:
        user_choice = "Paper"
    else:
        user_choice = "Scissors"

    print(name,"Choice: ",user_choice)
    print("=========================================")
    print("Now it is Computer's turn")

    computer = random.randint(1,3)

    if computer == 1:
        comp_choice = "Rock"
    elif computer == 2:
        comp_choice = "Paper"
    else:
        comp_choice = "Scissors"

    print("Computer's Choice: ",comp_choice)
    print("===============================================")
    if ((user_choice == "Paper" and comp_choice == "Rock") or (user_choice == "Rock" and comp_choice == "Paper")):
        if user_choice == "Paper":
            result = "Paper"
            print("!!! Paper Wins !!!")
            print(name,"Choice :",user_choice," And ", "Computers Choice :",comp_choice)
            print("===========================================")
            print("!!!!!! User won the game !!!!!!")
        else:
            result = "Paper"
            print("!!! Paper Wins !!!")
            print(name,"Choice :",user_choice," And ", "Computers Choice :",comp_choice)
            print("===========================================")
            print("!!!!!! Computer won the game !!!!!!")

    elif ((user_choice == "Rock" and comp_choice == "Scissors") or (user_choice == "Scissors" and comp_choice == "Rock")):
        if user_choice == "Rock":
            result = "Rock"
            print("!!! Rock win !!!")
            print(name,"Choice :",user_choice," And ", "Computers Choice :",comp_choice)
            print("==========================================")
            print("!!!!!! User won the game !!!!!!")
        else:
            result = "Rock"
            print("!!! Rock win !!!")
            print(name,"Choice :",user_choice," And ", "Computers Choice :",comp_choice)
            print("===========================================")
            print("!!!!!! Computer won the game !!!!!!")
    elif (user_choice == comp_choice ):
        result = "Tie"
        print(name,"Choice :",user_choice," And ", "Computers Choice :",comp_choice)
        print("===============================================")
        print("!!!!!! Game tie !!!!!!")
    else:
        if user_choice == "Scissors":
            result = "Scissors"
            print("!!! Scissors win !!!")
            print(name,"Choice :",user_choice," And ", "Computers Choice :",comp_choice)
            print("============================================")
            print("!!!!!! User won the game !!!!!!")
        else:
            result = "Scissors"
            print("!!! Scissors win !!!")
            print(name,"Choice :",user_choice," And ", "Computers Choice :",comp_choice)
            print("===========================================")
            print("!!!!!! Computer won the game !!!!!!")
    print()
    if result == "Tie":
        ties += 1
    elif result == user_choice:
        user_score += 1 
    else:
        comp_score += 1

    print("Scores are")
    print(name,"'s score is",user_score)
    print("Computer's Score: ",comp_score) 
    print("Ties :",ties)

    repeat = input("do you wnat to play again(y/n): ")
    if repeat == "n":
        break   

print("!!! Game over !!!")
print("!!! Thanks for playing !!!")