"""Write a function that takes a list of integers and returns a new list containing the
same values, but with all negative numbers converted to positive numbers."""

def converter(list1):
    list2 = []
    for i in list1:
        if i < 0:
            list2.append(-i)
        else:
            list2.append(i)
    return list2

list1 = [-1,-2,-3,4,-5]
print(converter(list1))

