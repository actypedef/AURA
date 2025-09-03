"""
Write a function to create a list of N empty dictionaries.
assert empty_list(5)==[{},{},{},{},{}]
"""
def empty_list(N):
    # Create a list comprehension that generates an empty dictionary for each iteration up to N
    return [{} for i in range(N)]

# Test the function with the provided test case
assert empty_list(5) == [{}, {}, {}, {}, {}]
