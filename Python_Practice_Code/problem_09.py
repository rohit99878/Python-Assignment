"""Write a Python program that prompts the user to input an integer and raises
 a ValueError exception if the input is not a valid integer.
"""
def get_integer_input(prompt):
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Error: Invalid input, input a valid integer.")
# Usage
n = get_integer_input("Input an integer: ")
print("Input value:", n)