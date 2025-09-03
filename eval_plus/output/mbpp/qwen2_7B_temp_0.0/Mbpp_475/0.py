"""
Write a function to sort a dictionary by value.
assert sort_counter({'Math':81, 'Physics':83, 'Chemistry':87})==[('Chemistry', 87), ('Physics', 83), ('Math', 81)]
"""
def sort_counter(dict):
    # Sort the dictionary by its values using sorted() and lambda as key
    sorted_dict = sorted(dict.items(), key=lambda x: x[1])
    return sorted_dict

# Test the function with the provided test case
assert sort_counter({'Math': 81, 'Physics': 83, 'Chemistry': 87}) == [('Chemistry', 87), ('Physics', 83), ('Math', 81)]
