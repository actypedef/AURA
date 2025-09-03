"""
Write a function to find the ration of positive numbers in an array of integers.
assert positive_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8])==0.54
"""
def positive_count(arr):
    # Count the number of positive elements in the array
    pos = sum(1 for i in arr if i > 0)
    
    # Calculate the ratio of positive elements to the total number of elements
    return round(pos / len(arr), 2)

# Test the function with the provided test case
assert positive_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]) == 0.54
