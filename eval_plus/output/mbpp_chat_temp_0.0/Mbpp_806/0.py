"""
Write a function to find maximum run of uppercase characters in the given string.
assert max_run_uppercase('GeMKSForGERksISBESt') == 5
"""
def max_run_uppercase(str1):
    # Initialize variables to keep track of the current run length and the maximum run length
    count = 0
    result = 0
    
    # Iterate through each character in the string
    for char in str1:
        # Check if the character is uppercase
        if char >= 'A' and char <= 'Z':
            # Increment the current run length
            count += 1
            # Update the maximum run length if the current run is longer
            result = max(result, count)
        else:
            # Reset the current run length if the character is not uppercase
            count = 0
            
    return result

# Test the function with the provided test case
assert max_run_uppercase('GeMKSForGERksISBESt') == 5