"""
Write a function to flatten the list of lists into a single set of numbers.
assert set(extract_singly([(3, 4, 5), (4, 5, 7), (1, 4)])) == set([3, 4, 5, 7, 1])
"""
def extract_singly(list_of_lists):
    # Flatten the list of lists using list comprehension
    flattened_list = [item for sublist in list_of_lists for item in sublist]
    # Convert the flattened list to a set to remove duplicates
    unique_numbers = set(flattened_list)
    return unique_numbers

# Test the function with provided data points
assert set(extract_singly([(3, 4, 5), (4, 5, 7), (1, 4)])) == set([3, 4, 5, 7, 1])