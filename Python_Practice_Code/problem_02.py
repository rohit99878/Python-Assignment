"""Write a function that takes a sentence as input and returns the
 sentence with each word reversed."""
def reverse_words(sentence):
    words = sentence.split()
    reversed_sentence = ' '.join(word[::-1] for word in words)
    return reversed_sentence

# Test case
print(reverse_words("Hello World"))  # "olleH dlroW"
