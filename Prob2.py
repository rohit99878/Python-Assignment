"""Write a function that takes a list of words and returns the longest word."""

temp = "This is a very long string with many words and characters"
temp1 = []
longest_word = ' '
temp1 = temp.split(' ')
for i in temp1:
    if len(i) > len(longest_word):
        longest_word = i
print(longest_word) 
