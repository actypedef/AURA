"""
Write a function to find the ration of positive numbers in an array of integers.
assert positive_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8])==0.54
"""
def positive_count(arr):
    # Initialize counters for positive numbers and total numbers
    pos_count = 0
    total_count = 0
    
    # Iterate through the array
    for num in arr:
        if num > 0:
            pos_count += 1  # Increment positive counter
        total_count += 1     # Increment total counter
    
    # Calculate the ratio of positive numbers
    ratio = pos_count / total_count
    return round(ratio, 2)  # Return the rounded ratio

# Test the function with the provided test case
assert positive_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]) == 0.54
