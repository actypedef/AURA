"""
Write a function that takes in a list and length n, and generates all combinations (with repetition) of the elements of the list and returns a list with a tuple for each combination.
assert combinations_colors( ["Red","Green","Blue"],1)==[('Red',), ('Green',), ('Blue',)]
"""
def combinations_colors(colors, n):
    # Base case: if n is 0, return a list containing an empty tuple
    if n == 0:
        return [()]
    
    # Initialize an empty list to store the result
    res = []
    
    # Iterate over each color in the input list
    for i in range(len(colors)):
        # Recursively call combinations_colors with reduced length n-1
        for c in combinations_colors(colors[i:], n - 1):
            # Append the current color and the recursive result as a tuple to the result list
            res.append((colors[i],) + c)
    
    # Return the final list of tuples representing combinations
    return res

# Test the function with the provided test case
assert combinations_colors(["Red", "Green", "Blue"], 1) == [('Red',), ('Green',), ('Blue',)]