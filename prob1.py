"""Write a function that takes a list of 
    numbers and returns the product of all the numbers."""

def mul(a):
    result = 1
    for i in a:
        result *= int(i)
    return result

a = []
while True:
    b = input("Enter number: ")
    if b == ' ':
        break
    a.append(b)
c = mul(a)
print(c)