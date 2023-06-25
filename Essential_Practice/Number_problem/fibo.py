"""
##########Fibonacci series :##############
a series of numbers in which each number ( Fibonacci number ) is the sum of 
the two preceding numbers. The simplest is the series 1, 1, 2, 3, 5, 8, etc.
"""
a = 0
b = 1
c = 0
d = int(input("Enter range : "))
for i in range(0,d):
    print(a)
    c = a + b
    a = b
    b = c