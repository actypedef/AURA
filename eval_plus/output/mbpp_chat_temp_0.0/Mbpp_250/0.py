"""
Write a python function that takes in a tuple and an element and counts the occcurences of the element in the tuple.
assert count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),4) == 0
"""
def count_X(test_tup, K):
    # Initialize counter to zero
    res = 0
    
    # Iterate through each element in the tuple
    for ele in test_tup:
        # Check if the current element matches the target element
        if ele == K:
            # Increment counter if match found
            res += 1
            
    return res

# Test the function with the provided test case
assert count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2), 4) == 0