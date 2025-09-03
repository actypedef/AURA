"""
Write a python function to find the minimum difference between any two elements in a given array. https://www.geeksforgeeks.org/find-minimum-difference-pair/
assert find_min_diff((1,5,3,19,18,25),6) == 1
"""
def find_min_diff(arr, n):
    # Sort the array to bring close elements together
    arr.sort()
    
    # Initialize min_diff with a large number
    min_diff = float('inf')
    
    # Iterate through the sorted array to find the minimum difference
    for i in range(0, n-1):
        diff = arr[i+1] - arr[i]
        if diff < min_diff:
            min_diff = diff
    
    return min_diff

# Test the function with the provided test case
assert find_min_diff((1, 5, 3, 19, 18, 25), 6) == 1