"""Write a function to check if two given strings are anagrams 
(contain the same characters in any order)."""
def is_anagram(str1, str2):
    return sorted(str1.lower()) == sorted(str2.lower())

# Test cases
print(is_anagram("listen", "silent"))  # True
print(is_anagram("hello", "world"))  # False
