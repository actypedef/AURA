"""
Write a function to reverse each string in a given list of string values.
assert reverse_string_list(['Red', 'Green', 'Blue', 'White', 'Black'])==['deR', 'neerG', 'eulB', 'etihW', 'kcalB']
"""
def reverse_string_list(string_list):
    # Reverse each string in the list using list comprehension
    reversed_strings = [s[::-1] for s in string_list]
    return reversed_strings

# Test the function with the provided test case
assert reverse_string_list(['Red', 'Green', 'Blue', 'White', 'Black']) == ['deR', 'neerG', 'eulB', 'etihW', 'kcalB']
