"""Write a function that takes a list of numbers and returns the difference between 
the largest and smallest numbers."""

def difference(list1):
    list1.sort()
    diff = list1[-1] - list1[0]
    return diff

list1 = [90,50,10,40,30]
print(difference(list1))