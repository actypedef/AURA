"""
Write a function that takes in a list and length n, and generates all combinations (with repetition) of the elements of the list and returns a list with a tuple for each combination.
assert combinations_colors( ["Red","Green","Blue"],1)==[('Red',), ('Green',), ('Blue',)]
"""
def combinations_colors(colors, n):
    # Initialize an empty list to store the combinations
    result = []
    
    # Helper function to generate combinations recursively
    def combine(current_combination, remaining_elements):
        if len(current_combination) == n:
            result.append(tuple(current_combination))
            return
        for element in remaining_elements:
            current_combination.append(element)
            combine(current_combination, remaining_elements)
            current_combination.pop()  # Backtrack to explore other combinations
    
    # Start the recursive combination generation from the full list of colors
    combine([], colors)
    
    return result

# Test the function with the provided test case
assert combinations_colors(["Red", "Green", "Blue"], 1) == [('Red',), ('Green',), ('Blue',)]