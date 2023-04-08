"""Write a function that takes two lists and returns a new list
 containing only the elements that are common to both lists."""

def duplicate(list1,list2):
    for i in list1:
        if i in list2 and i not in list3:
                list3.append(i)
    return list3




list1 = ['Hello','How','Are', 'You','am']
list2 = ['Hello','I','am', 'fine', 'and','You']
list3 = []
result = duplicate(list1,list2)
print(result)