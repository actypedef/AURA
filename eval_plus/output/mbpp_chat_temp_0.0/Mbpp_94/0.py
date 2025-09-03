"""
Given a list of tuples, write a function that returns the first value of the tuple with the smallest second value.
assert index_minimum([('Rash', 143), ('Manjeet', 200), ('Varsha', 100)]) == 'Varsha'
"""
def index_minimum(test_list):
    # Find the tuple with the minimum second element and return its first element
    res = min(test_list, key=lambda x: x[1])[0]
    return res

# Test the function with the provided test case
assert index_minimum([('Rash', 143), ('Manjeet', 200), ('Varsha', 100)]) == 'Varsha'
