"""
Iterator : An iterator is an object that contains a countable number of values. 
An iterator is an object that can be iterated upon, meaning that you can traverse 
through all the values. Technically, in Python, an iterator is an object which 
implements the iterator protocol, which consist of the methods iter() and next() .

"""

a = [1,2,3,4,5]

it = iter(a)

######################################################
print(it.__next__()) # 1st method
print(it.__next__())
######################################################

######################################################
print(next(it))     # 2nd Method
######################################################

for i in it:
    print(i)