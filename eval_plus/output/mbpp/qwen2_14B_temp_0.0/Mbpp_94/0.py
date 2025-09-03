"""
Given a list of tuples, write a function that returns the first value of the tuple with the smallest second value.
assert index_minimum([('Rash', 143), ('Manjeet', 200), ('Varsha', 100)]) == 'Varsha'
"""
def index_minimum(list1):
    # Find the tuple with the smallest second value
    min_value = min(list1, key=lambda x: x[1])
    # Return the first value of the found tuple
    return min_value[0]

# Test the function with the provided test case
assert index_minimum([('Rash', 143), ('Manjeet', 200), ('Varsha', 100)]) == 'Varsha'
