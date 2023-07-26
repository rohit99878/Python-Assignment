"""Write a function that calculates the difference between the sum of
 squares and the square of sums for a given range of numbers."""
def sum_square_difference(n):
    sum_of_squares = sum(i ** 2 for i in range(1, n + 1))
    square_of_sum = sum(range(1, n + 1)) ** 2
    return square_of_sum - sum_of_squares

# Test case
print(sum_square_difference(10))  # 2640
