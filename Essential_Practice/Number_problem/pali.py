"""
############## Palindrome Number ####################
There are 90 palindromic numbers with three digits (Using the Rule of product:
9 choices for the first digit - which determines the third digit as well - 
multiplied by 10 choices for the second digit): {101, 111, 121, 131, 141, 151,
 161, 171, 181, 191, …, 909, 919, 929, 939, 949, 959, 969, 979, 989, 999}
 """


a = 101
b = a
rev = 0
while b > 0 :
    c = b%10
    rev = (rev*10)+ c
    b = b // 10

if rev == a:
    print("Palindrome")
else:
    print("Not Palindrome")