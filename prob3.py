"""Write a function that takes a list of integers and 
returns a new list containing only the prime numbers."""

def find_prime(list):
    prime = []
    for i in (list):
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            if i > 1:
                prime.append(i)
    return prime

list = [1,2,3,4,5,6,7,8,9,10]
prime_numb = find_prime(list)
print(prime_numb)
