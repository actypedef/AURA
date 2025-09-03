"""
Write a function to remove all whitespaces from a string.
assert remove_all_spaces('python  program')==('pythonprogram')
"""
def remove_all_spaces(str1):
    # Initialize an empty string to store the result
    str2 = ""
    
    # Iterate through each character in the input string
    for i in range(len(str1)):
        # Check if the current character is not a whitespace
        if str1[i] != " ":
            # Append the non-whitespace character to the result string
            str2 += str1[i]
    
    # Return the resulting string without any spaces
    return str2

# Test the function with the provided test case
assert remove_all_spaces('python  program') == 'pythonprogram'
