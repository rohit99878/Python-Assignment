list1 = [1,"Rohit",10.20]
print(list1)

#print(''.join(list1))  # If all elements are string

for i in list1:  #Here we accessing elements driectly.
    print(i)

for i in range(len(list1)): #Indexing
    print(i)

######## Slicing ##########

print(list1[::])
print(list1[::-1])
print(list1[2])
