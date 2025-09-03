"""
Write a python function to find the minimum difference between any two elements in a given array. https://www.geeksforgeeks.org/find-minimum-difference-pair/
assert find_min_diff((1,5,3,19,18,25),6) == 1
"""
def find_min_diff(arr, k):
    arr.sort()  # Sort the array
    min_diff = float('inf')  # Initialize min_diff as infinity
    for i in range(len(arr)-1):  # Iterate through the array
        if arr[i+1] - arr[i] < min_diff:  # Check if current difference is smaller than min_diff
            min_diff = arr[i+1] - arr[i]  # Update min_diff
    return min_diff

# Test the function
assert find_min_diff((1,5,3,19,18,25),6) == 1