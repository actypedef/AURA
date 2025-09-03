"""
Write a python function that takes in a tuple and an element and counts the occcurences of the element in the tuple.
assert count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),4) == 0
"""
# Define a function to count occurrences of an element in a tuple
def count_X(test_tup, K):
    # Initialize a counter to zero
    res = 0
    
    # Iterate through each element in the tuple
    for ele in test_tup:
        # Check if the current element matches the target element
        if ele == K:
            # Increment the counter if there's a match
            res += 1
            
    # Return the total count of occurrences
    return res

# Test the function with provided data points
assert count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2), 4) == 0