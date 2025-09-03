"""
Write a function to find the difference of the first even and first odd number of a given list.
assert diff_even_odd([1,3,5,7,4,1,6,8])==3
"""
def diff_even_odd(lst):
    # Find the index of the first even number
    even_index = next((i for i, x in enumerate(lst) if x % 2 == 0), None)
    
    # Find the index of the first odd number
    odd_index = next((i for i, x in enumerate(lst) if x % 2 != 0), None)
    
    # Calculate the difference between the first even and first odd numbers
    return lst[even_index] - lst[odd_index]

# Test the function
assert diff_even_odd([1,3,5,7,4,1,6,8]) == 3