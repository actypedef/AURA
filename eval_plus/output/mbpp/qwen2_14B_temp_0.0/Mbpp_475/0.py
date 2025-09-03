"""
Write a function to sort a dictionary by value.
assert sort_counter({'Math':81, 'Physics':83, 'Chemistry':87})==[('Chemistry', 87), ('Physics', 83), ('Math', 81)]
"""
def sort_counter(dict1):
    # Sort the dictionary by value and return a list of tuples
    sorted_dict = sorted(dict1.items(), key=lambda x: x[1])
    return sorted_dict

# Test the function with the provided test case
assert sort_counter({'Math': 81, 'Physics': 83, 'Chemistry': 87}) == [('Chemistry', 87), ('Physics', 83), ('Math', 81)]
