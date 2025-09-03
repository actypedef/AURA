"""
Write a function that takes in a sorted array, its length (n), and an element and returns whether the element is the majority element in the given sorted array. (The majority element is the element that occurs more than n/2 times.)
assert is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3) == True
"""
def is_majority(arr, n, x):
    # Check if the element is present in the array
    if x not in arr:
        return False
    
    # Count occurrences of the element
    count = arr.count(x)
    
    # Check if the count is greater than n/2
    if count > n // 2:
        return True
    else:
        return False

# Test cases to verify the correctness of the function
assert is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3) == True
assert is_majority([1, 2, 3, 4, 5], 5, 6) == False
assert is_majority([1, 1, 1, 1, 1], 5, 1) == True
assert is_majority([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10, 10) == True
assert is_majority([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10, 11) == False