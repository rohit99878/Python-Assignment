"""
Armstrong Number :
An Armstrong number is one whose sum of digits raised to the power three 
equals the number itself. 371, for example, is an Armstrong number because 
33 + 73 + 1**3 = 371
"""

a = int(input("Enter : "))
b = a
mul = 0
while b>0:
    arm = b % 10
    mul += arm*arm*arm
    b = b // 10
if a == mul:
    print("arm")
else:
    print("not arm")