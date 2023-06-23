##### Python Functions #####
list1 = [10,20,30,40,50]


#1. Len Function.
a = len(list1) 
print("Len :",a)       #op -> 5


#2. Max Function :-> It is only work with numric numbers
a = max(list1)
print("Max number :",a)


#3. Min Function :-> 
a = min(list1)
print("Min number :",a)


#4. Sum Function
a = sum(list1)
print("Sum number :",a)


#5. Sorted Function
print("Sorted List: ",sorted(list1))


#6. Reversed Function
print(list(reversed(list1)))
#a = reversed(list1) ## Shows only a address
#print("Reversed List: ",a)


#7 Enumerate Function
print(list(enumerate(list1, 0)))
# Op -> [(0, 10), (1, 20), (2, 30), (3, 40), (4, 50)]


#8 map()
print(list(map(lambda x: x+2, list1)))


#9 filter()



#10 zip()


#13) iter()


#14) all()


#15) any()