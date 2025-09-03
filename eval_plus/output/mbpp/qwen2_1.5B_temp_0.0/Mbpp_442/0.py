"""
Write a function to find the ration of positive numbers in an array of integers.
assert positive_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8])==0.54
"""
def positive_count(arr):
    # Count the number of positive numbers in the array
    count = sum(1 for num in arr if num > 0)
    
    # Calculate the total number of elements in the array
    total_elements = len(arr)
    
    # Calculate the ratio of positive numbers
    ratio = count / total_elements
    
    return ratio

# Test the function with the provided test case
assert positive_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]) == 0.54