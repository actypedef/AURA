"""
Write a function to reverse each string in a given list of string values.
assert reverse_string_list(['Red', 'Green', 'Blue', 'White', 'Black'])==['deR', 'neerG', 'eulB', 'etihW', 'kcalB']
"""
def reverse_string_list(string_list):
    # Use list comprehension to reverse each string in the list
    reversed_list = [s[::-1] for s in string_list]
    return reversed_list

# Test the function with provided data points
assert reverse_string_list(['Red', 'Green', 'Blue', 'White', 'Black']) == ['deR', 'neerG', 'eulB', 'etihW', 'kcalB']