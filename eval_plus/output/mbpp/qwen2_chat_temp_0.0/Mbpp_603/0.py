"""
Write a function to get all lucid numbers smaller than or equal to a given integer.
assert get_ludic(10) == [1, 2, 3, 5, 7]
"""
def get_ludic(n):
    # Initialize the list of ludic numbers with the first two ludic numbers
    ludics = [1, 2]
    
    # Continue generating ludic numbers until the last one is greater than n
    while ludics[-1] < n:
        next_ludic = ludics[-1] + ludics[-2]
        if next_ludic > n:
            break
        ludics.append(next_ludic)
    
    return ludics

# Test the function with the provided test case
assert get_ludic(10) == [1, 2, 3, 5, 7]