"""
Write a function to find maximum run of uppercase characters in the given string.
assert max_run_uppercase('GeMKSForGERksISBESt') == 5
"""
def max_run_uppercase(s):
    # Initialize variables to keep track of the current run length and the maximum run length found
    current_run = 0
    max_run = 0
    
    # Iterate through each character in the string
    for char in s:
        # If the character is uppercase, increment the current run length
        if char.isupper():
            current_run += 1
        else:
            # If the character is not uppercase, reset the current run length
            current_run = 0
        
        # Update the maximum run length if the current run length is greater
        if current_run > max_run:
            max_run = current_run
    
    return max_run

# Test cases to verify the correctness of the function
assert max_run_uppercase('GeMKSForGERksISBESt') == 5
assert max_run_uppercase('abcdefg') == 0
assert max_run_uppercase('ABCDEFG') == 7
assert max_run_uppercase('aAaaaBbBb') == 4
assert max_run_uppercase('AaaAaaaBbbBb') == 6