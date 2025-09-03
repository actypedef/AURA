"""
Write a function that takes as input a tuple of numbers (t_1,...,t_{N+1}) and returns a tuple of length N where the i-th element of the tuple is equal to t_i * t_{i+1}.
assert multiply_elements((1, 5, 7, 8, 10)) == (5, 35, 56, 80)
"""
def multiply_elements(tup):
    # Initialize an empty list to store the result
    result = []
    
    # Iterate through the tuple using range(len(tup) - 1)
    for i in range(len(tup) - 1):
        # Multiply each pair of adjacent elements and append to the result list
        result.append(tup[i] * tup[i + 1])
    
    # Convert the result list back to a tuple and return it
    return tuple(result)

# Test the function with the provided test case
assert multiply_elements((1, 5, 7, 8, 10)) == (5, 35, 56, 80)