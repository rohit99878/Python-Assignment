"""Write a Python program that prompts the user to input two numbers and raises
 a TypeError exception if the inputs are not numerical.
"""
def get_numeric_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Error: Invalid input. Please Input a valid number.")
# Usage
n1 = get_numeric_input("Input the first number: ")
n2 = get_numeric_input("Input the second number: ")
result = n1 * n2
print("Product of the said two numbers:", result)