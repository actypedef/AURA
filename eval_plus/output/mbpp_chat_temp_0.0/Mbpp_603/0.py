"""
Write a function to get all lucid numbers smaller than or equal to a given integer.
assert get_ludic(10) == [1, 2, 3, 5, 7]
"""
def get_ludic(n):
    # Initialize the list of ludic numbers with the first two numbers
    ludics = [1, 2]
    
    # Iterate from 3 up to n to find ludic numbers
    for i in range(3, n + 1):
        # Check if the number is not divisible by any previous ludic number
        if all(i % j != 0 for j in ludics):
            ludics.append(i)
    
    # Return the list of ludic numbers less than or equal to n
    return ludics

# Test the function with the provided test case
assert get_ludic(10) == [1, 2, 3, 5, 7]
