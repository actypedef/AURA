"""
Write a function that takes in an array and element and returns a tuple containing a boolean that indicates if the element is in the array and the index position of the element (or -1 if the element is not found).
assert sequential_search([11,23,58,31,56,77,43,12,65,19],31) == (True, 3)
"""
def sequential_search(arr, x):
    # Iterate through each element in the array
    for i in range(len(arr)):
        # Check if the current element matches the target value
        if arr[i] == x:
            # Return True and the index of the element
            return (True, i)
    # If no match is found, return False and -1
    return (False, -1)

# Test the function with the provided test case
assert sequential_search([11, 23, 58, 31, 56, 77, 43, 12, 65, 19], 31) == (True, 3)
