####### List Methods ########

#1. list.append()	:: Adds a new item at the end of the list.

list1 = [10,20,30,40,50]
list1.append(60)
print(list1)


#2. list.clear()	:: Removes all the items from the list and make it empty.

list1 = [10,20,30,40,50]
list1.clear()
print(list1)


#3. list.copy()     :: Returns a shallow copy of a list.

list1 = [10,20,30,40,50]
list2 = list1.copy()


#4. list.count()	:: Returns the number of times an element occurs in the list.

list1 = [10,20,30,40,50]
print("Count is :",list1.count(10))


#5. list.extend()	:: Adds all the items of the specified iterable (list, 
# tuple, set, dictionary, string) to the end of the list.

list1 = [10,20,30,40,50]
list2 = [60,70,80]
list1.extend(list2)
print(list1)


#6. list.index()	:: Returns the index position of the first occurance 
# of the specified item. Raises a ValueError if there is no item found.

list1 = [10,20,30,40,50]
print("Index :",list1.index(20))



#7. list.insert()	:: Inserts an item at a given position.

list1 = [10,20,30,40,50]
list1.insert(5,90)
print(list1)


#8. list.pop()	    :: Returns an item from the specified index position and
#also removes it from the list. If no index is specified, the list.pop() method 
# removes and returns the last item in the list.

list1 = [10,20,30,40,50]
list1.pop(4)
print(list1)

#9. list.remove()	:: Removes the first occurance of the specified item from
#  the list. It the specified item not found then throws a ValueError.

list1 = [10,20,30,40,50]
list1.remove(20)
print(list1)


#10. list.reverse()	:: Reverses the index positions of the elements in the list.
#  The first element will be at the last index, the second element will be at
#  second last index and so on.

list1 = [10,20,30,40,50]
list1.reverse()
print(list1)


#11. list.sort()	:: Sorts the list items in ascending, descending,
#or in custom order.

list1 = [10,20,30,40,50]
list1.sort()
print(list1)