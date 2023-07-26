"""Write a function that takes a list of integers and finds the largest 
continuous sum (sum of any subset of adjacent elements)."""

def max_continuous_sum(arr):
    max_sum = current_sum = arr[0]
    for num in arr[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum

# Test case
print(max_continuous_sum([1, 2, -1, 3, 4, -1]))  # 9
