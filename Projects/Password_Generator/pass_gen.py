import random
import string

def generate_password(length, include_uppercase, include_lowercase, include_numbers, include_special_chars):
    characters = ''
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_numbers:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation

    if not characters:
        print("Error: Please select at least one character type.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Random Password Generator!\n")

    length = int(input("Enter the desired password length: "))
    include_uppercase = input("Do you want to include uppercase letters? (y/n): ").lower() == 'y'
    include_lowercase = input("Do you want to include lowercase letters? (y/n): ").lower() == 'y'
    include_numbers = input("Do you want to include numbers? (y/n): ").lower() == 'y'
    include_special_chars = input("Do you want to include special characters? (y/n): ").lower() == 'y'

    password = generate_password(length, include_uppercase, include_lowercase, include_numbers, include_special_chars)

    if password:
        print("\nGenerated Password:", password)

if __name__ == "__main__":
    main()
