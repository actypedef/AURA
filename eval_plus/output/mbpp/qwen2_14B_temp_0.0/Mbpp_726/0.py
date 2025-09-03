"""
Write a function that takes as input a tuple of numbers (t_1,...,t_{N+1}) and returns a tuple of length N where the i-th element of the tuple is equal to t_i * t_{i+1}.
assert multiply_elements((1, 5, 7, 8, 10)) == (5, 35, 56, 80)
"""
def multiply_elements(test_tup):
    # Create a new tuple where each element is the product of consecutive elements from the input tuple
    res = tuple(test_tup[i] * test_tup[i + 1] for i in range(len(test_tup) - 1))
    return res

# Test the function with the provided test case
assert multiply_elements((1, 5, 7, 8, 10)) == (5, 35, 56, 80)
