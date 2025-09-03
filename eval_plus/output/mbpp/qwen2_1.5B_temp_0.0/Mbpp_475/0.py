"""
Write a function to sort a dictionary by value.
assert sort_counter({'Math':81, 'Physics':83, 'Chemistry':87})==[('Chemistry', 87), ('Physics', 83), ('Math', 81)]
"""
def sort_counter(counter):
    # Sort the counter items based on their values in descending order
    sorted_items = sorted(counter.items(), key=lambda item: item[1], reverse=True)
    return sorted_items

# Test the function with provided data points
assert sort_counter({'Math':81, 'Physics':83, 'Chemistry':87}) == [('Chemistry', 87), ('Physics', 83), ('Math', 81)]