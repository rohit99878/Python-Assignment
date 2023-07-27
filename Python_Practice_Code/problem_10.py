"""Write a Python program that opens a file and handles a FileNotFoundError 
exception if the file does not exist."""
def open_file(filename):
    try:
        file = open(filename, 'r')
        contents = file.read()
        print("File contents:")
        print(contents)
        file.close()
    except FileNotFoundError:
        print("Error: File not found.")
# Usage
file_name = input("Input a file name: ")
open_file(file_name)