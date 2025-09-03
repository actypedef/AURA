"""
Write a function to find maximum run of uppercase characters in the given string.
assert max_run_uppercase('GeMKSForGERksISBESt') == 5
"""
def max_run_uppercase(str):
    # Initialize variables to track the current run length and the maximum run length
    curr = 0
    mx = 0
    
    # Iterate through each character in the string
    for i in range(len(str)):
        # Check if the current character is an uppercase letter
        if str[i].isupper():
            # Increment the current run length
            curr += 1
        else:
            # Update the maximum run length if the current run is longer
            mx = max(curr, mx)
            # Reset the current run length
            curr = 0
    
    # Final check to update the maximum run length for the last sequence
    mx = max(mx, curr)
    
    return mx

# Test the function with the provided test case
assert max_run_uppercase('GeMKSForGERksISBESt') == 5