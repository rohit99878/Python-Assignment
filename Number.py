import random

lower = int(input("Enter lower number: "))
upper = int(input("Enter upper number: "))

a = random.randint(lower,upper)

chance = 0
while True:
    print("Guess a number between {0} and {1}".format(lower, upper))
    print("You have {0} guesses left".format(7 - chance))
    user = int(input("Enter your guess: "))
    if user == a:
        print("Congratulations! You guessed the secret number in {0} guesses".format(chance + 1))
        break
    elif user < a:
        print("Your guess is too low")
    else:
        print("Your guess is too high")
    chance += 1
    if chance == 7:
        print("Sorry, you ran out of guesses. The secret number was {0}".format(a))
        break