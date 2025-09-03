"""
Write a python function to check whether every even index contains even numbers of a given list.
assert even_position([3,2,1]) == False
"""
def even_position(lst):
    # Iterate over the list using enumerate to get both index and value
    for i, num in enumerate(lst):
        # Check if the index is even and the number at that index is odd
        if i % 2 == 0 and num % 2 != 0:
            return False
    # If no such pair is found, return True
    return True

# Test cases
assert even_position([3,2,1]) == False
assert even_position([4,6,8,10]) == True
assert even_position([5,7,9,11]) == False
assert even_position([2,4,6,8]) == True