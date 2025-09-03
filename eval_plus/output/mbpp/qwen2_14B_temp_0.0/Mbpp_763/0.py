"""
Write a python function to find the minimum difference between any two elements in a given array. https://www.geeksforgeeks.org/find-minimum-difference-pair/
assert find_min_diff((1,5,3,19,18,25),6) == 1
"""
def find_min_diff(arr, n):
    # Sort the array to bring closest elements next to each other
    arr = sorted(arr)
    
    # Initialize the minimum difference to a large number
    min_diff = float('inf')
    
    # Iterate through the array to find the minimum difference
    for i in range(n - 1):
        if arr[i + 1] - arr[i] < min_diff:
            min_diff = arr[i + 1] - arr[i]
    
    return min_diff

# Test the function with the provided test case
assert find_min_diff((1, 5, 3, 19, 18, 25), 6) == 1
