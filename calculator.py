def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("Welcome to the calculator program!")
print("Please select an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

# Ask the user to enter their choice of operation
while True:
    try:
        choice = int(input("Enter your choice (1-4): "))
        if choice not in [1, 2, 3, 4]:
            raise ValueError
        break
    except ValueError:
        print("Invalid choice. Please enter a number between 1 and 4.")

# Ask the user to enter two numbers
while True:
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        break
    except ValueError:
        print("Invalid input. Please enter a number.")

# Perform the selected operation and display the result
if choice == 1:
    result = add(num1, num2)
    print("{} + {} = {}".format(num1, num2, result))
elif choice == 2:
    result = subtract(num1, num2)
    print("{} - {} = {}".format(num1, num2, result))
elif choice == 3:
    result = multiply(num1, num2)
    print("{} x {} = {}".format(num1, num2, result))
elif choice == 4:
    if num2 == 0:
        print("Error: Division by zero")
    else:
        result = divide(num1, num2)
        print("{} / {} = {}".format(num1, num2, result))
