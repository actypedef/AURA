"""
Write a function to get all lucid numbers smaller than or equal to a given integer.
assert get_ludic(10) == [1, 2, 3, 5, 7]
"""
def get_ludic(n):
    # Initialize the list of ludic numbers with the first two elements
    ludics = [1, 2]
    
    # Generate ludic numbers until we reach or exceed n
    while len(ludics) <= n:
        next_ludic = len(ludics)
        ludics.append(next_ludic)
        
        # Remove the element at position 'next_ludic' from the list
        if next_ludic < len(ludics):
            del ludics[next_ludic]
    
    # Return the ludic numbers up to the nth element
    return ludics[:n]

# Test the function with the provided test case
assert get_ludic(10) == [1, 2, 3, 5, 7]
