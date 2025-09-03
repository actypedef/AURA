"""
Write a function to get all lucid numbers smaller than or equal to a given integer.
assert get_ludic(10) == [1, 2, 3, 5, 7]
"""
def get_ludic(n):
    ludics = list(range(1, n + 1))  # Initialize the list of ludic numbers from 1 to n
    index = 1
    
    while index != len(ludics):
        first_ludic = ludics[index]  # Get the current ludic number
        remove_index = index + first_ludic  # Calculate the index of the next number to remove
        
        while remove_index < len(ludics):
            ludics.remove(ludics[remove_index])  # Remove the number at the calculated index
            remove_index += first_ludic - 1  # Update the remove_index for the next iteration
        
        index += 1
    
    return ludics

# Test the function with the provided test case
assert get_ludic(10) == [1, 2, 3, 5, 7]
