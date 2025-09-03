"""
Write a function to count the number of occurence of the string 'std' in a given string.
assert count_occurance("letstdlenstdporstd") == 3
"""
def count_occurance(str1):
    # Initialize count to zero
    count = 0
    
    # Iterate through the string to check for occurrences of 'std'
    for i in range(len(str1) - 2):
        if str1[i:i+3] == 'std':
            count += 1
            
    return count

# Test the function with the provided test case
assert count_occurance("letstdlenstdporstd") == 3
