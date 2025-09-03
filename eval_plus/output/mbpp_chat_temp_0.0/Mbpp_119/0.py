"""
Write a python function to find the element that appears only once in a sorted array.
assert search([1,1,2,2,3]) == 3
"""
def search(arr):
    # Iterate through the array in steps of 2
    for i in range(0, len(arr) - 1, 2):
        # Check if the current element is not equal to the next one
        if arr[i] != arr[i + 1]:
            return arr[i]
    # If no unique element is found, return the last element
    return arr[-1]

# Test the function with the provided test case
assert search([1, 1, 2, 2, 3]) == 3
