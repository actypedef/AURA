"""
Write a function to move all the numbers to the end of the given string.
assert move_num('I1love143you55three3000thousand') == 'Iloveyouthreethousand1143553000'
"""
def move_num(s):
    # Initialize an empty list to store non-numeric characters
    non_nums = []
    
    # Iterate through each character in the string
    for i in s:
        # Check if the character is not a digit
        if not i.isdigit():
            # Append the non-numeric character to the list
            non_nums.append(i)
    
    # Join the non-numeric characters back into a string
    non_nums_str = ''.join(non_nums)
    
    # Return the concatenated result of non-numeric characters followed by numeric characters
    return non_nums_str + ''.join(filter(str.isdigit, s))

# Test the function with the provided test case
assert move_num('I1love143you55three3000thousand') == 'Iloveyouthreethousand1143553000'
