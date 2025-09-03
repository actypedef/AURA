"""
Write a function to count the number of occurence of the string 'std' in a given string.
assert count_occurance("letstdlenstdporstd") == 3
"""
def count_occurance(s):
    # Initialize a counter for occurrences of 'std'
    count = 0
    
    # Iterate through the string using a loop
    for i in range(len(s) - 2):  # Subtract 2 to avoid index out of range error
        # Check if the substring from current index to next 3 characters is 'std'
        if s[i:i+3] == "std":
            count += 1  # Increment the counter if condition is met
    
    return count

# Test the function with the provided test case
assert count_occurance("letstdlenstdporstd") == 3