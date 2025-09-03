"""
Write a function that takes as input a tuple of numbers (t_1,...,t_{N+1}) and returns a tuple of length N where the i-th element of the tuple is equal to t_i * t_{i+1}.
assert multiply_elements((1, 5, 7, 8, 10)) == (5, 35, 56, 80)
"""
def multiply_elements(test_tup):
    # Initialize an empty list to store the results
    res = []
    # Iterate over the tuple using index
    for i in range(len(test_tup) - 1):
        # Multiply the current element with the next one and append to the result list
        res.append(test_tup[i] * test_tup[i + 1])
    # Convert the list to a tuple and return it
    return tuple(res)

# Test the function with the provided test case
assert multiply_elements((1, 5, 7, 8, 10)) == (5, 35, 56, 80)
