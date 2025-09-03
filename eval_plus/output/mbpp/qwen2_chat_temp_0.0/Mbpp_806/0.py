"""
Write a function to find maximum run of uppercase characters in the given string.
assert max_run_uppercase('GeMKSForGERksISBESt') == 5
"""
def max_run_uppercase(s):
    # Initialize variables to keep track of the current run length and the maximum run length
    curr_run = 0
    max_run = 0
    
    # Iterate through each character in the string
    for i in range(len(s)):
        # Check if the current character is uppercase
        if s[i].isupper():
            # Increment the current run length
            curr_run += 1
            # Update the maximum run length if the current run is longer
            max_run = max(max_run, curr_run)
        else:
            # Reset the current run length if the character is not uppercase
            curr_run = 0
            
    return max_run

# Test the function with the provided test case
assert max_run_uppercase('GeMKSForGERksISBESt') == 5
