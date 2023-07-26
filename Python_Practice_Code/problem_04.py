"""Write a function that takes a sentence as input and returns a dictionary
 containing the count of each word."""

def word_count(sentence):
    words = sentence.split()
    word_freq = {}
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1
    return word_freq

# Test case
print(word_count("hello world hello"))  # {'hello': 2, 'world': 1}
