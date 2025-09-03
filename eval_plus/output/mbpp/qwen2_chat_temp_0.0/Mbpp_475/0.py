"""
Write a function to sort a dictionary by value.
assert sort_counter({'Math':81, 'Physics':83, 'Chemistry':87})==[('Chemistry', 87), ('Physics', 83), ('Math', 81)]
"""
def sort_counter(dict):
    # Sort the dictionary by its values using sorted() function and lambda as key
    return sorted(dict.items(), key=lambda x: x[1])

# Test the function with the provided test case
assert sort_counter({'Math': 81, 'Physics': 83, 'Chemistry': 87}) == [('Chemistry', 87), ('Physics', 83), ('Math', 81)]
