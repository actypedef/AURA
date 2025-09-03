"""
Write a function to count the total number of characters in a string.
assert count_charac("python programming")==18
"""
def count_charac(str):
    # Initialize a counter variable to zero
    count = 0
    # Iterate over each character in the string
    for char in str:
        # Increment the counter for each character encountered
        count += 1
    # Return the total count of characters
    return count

# Test the function with the provided test case
assert count_charac("python programming") == 18
