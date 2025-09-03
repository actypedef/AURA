"""
Write a function to create a list of N empty dictionaries.
assert empty_list(5)==[{},{},{},{},{}]
"""
def empty_list(length):
    # Create a list of empty dictionaries using list comprehension
    empty_list = [{} for _ in range(length)]
    return empty_list

# Test the function with the provided test case
assert empty_list(5) == [{}, {}, {}, {}, {}]
