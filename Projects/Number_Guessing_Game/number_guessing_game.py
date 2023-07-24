import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I have picked a random number between 1 and 100.")

    # Set the range for the random number (you can modify this if desired)
    min_number = 1
    max_number = 100
    secret_number = random.randint(min_number, max_number)

    attempts = 0
    max_attempts = 10

    while attempts < max_attempts:
        print(f"\nAttempts remaining: {max_attempts - attempts}")
        guess = int(input("Enter your guess: "))

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed the number correctly!")
            break

        attempts += 1

    if attempts == max_attempts:
        print(f"\nGame over! The secret number was {secret_number}.")

def main():
    number_guessing_game()

if __name__ == "__main__":
    main()
