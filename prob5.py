"""Write a function that takes a string and returns a dictionary with
 the count of each character in the string."""

def find_word_count(string1):
    dict = { }
    for i in string1:
        if i in dict:
            dict[i] +=1
        else:
            dict[i] = 1
    return dict

string1 = "Hello world"
result = find_word_count(string1)
print(result)
        