"""
Write a function to count the number of occurence of the string 'std' in a given string.
assert count_occurance("letstdlenstdporstd") == 3
"""
def count_occurance(s):
    return s.count('std')

# Test cases
assert count_occurance("letstdlenstdporstd") == 3
assert count_occurance("stdstdstd") == 4
assert count_occurance("no_std_here") == 0
assert count_occurance("std123std456std789") == 6