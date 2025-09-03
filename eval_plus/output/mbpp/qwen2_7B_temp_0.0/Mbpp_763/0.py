"""
Write a python function to find the minimum difference between any two elements in a given array. https://www.geeksforgeeks.org/find-minimum-difference-pair/
assert find_min_diff((1,5,3,19,18,25),6) == 1
"""
def find_min_diff(arr, n):
    # Initialize the minimum difference as a large number
    min_diff = float('inf')
    
    # Sort the array to make it easier to find the smallest difference
    arr.sort()
    
    # Iterate through the sorted array and calculate the difference between consecutive elements
    for i in range(0, n - 1):
        diff = arr[i + 1] - arr[i]
        
        # Update the minimum difference if the current difference is smaller
        if diff < min_diff:
            min_diff = diff
    
    return min_diff

# Test the function with the provided test case
assert find_min_diff((1, 5, 3, 19, 18, 25), 6) == 1
