"""
Given a list of tuples, write a function that returns the first value of the tuple with the smallest second value.
assert index_minimum([('Rash', 143), ('Manjeet', 200), ('Varsha', 100)]) == 'Varsha'
"""
def index_minimum(tuples_list):
    # Find the tuple with the minimum second value
    min_tuple = min(tuples_list, key=lambda x: x[1])
    # Return the first value of the found tuple
    return min_tuple[0]

# Test cases to verify the correctness of the solution
assert index_minimum([('Rash', 143), ('Manjeet', 200), ('Varsha', 100)]) == 'Varsha'
assert index_minimum([('John', 56), ('Anna', 78), ('Peter', 90)]) == 'Anna'
assert index_minimum([('Alice', 34), ('Bob', 23), ('Charlie', 45)]) == 'Bob'