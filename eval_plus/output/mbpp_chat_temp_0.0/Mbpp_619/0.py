"""
Write a function to move all the numbers to the end of the given string.
assert move_num('I1love143you55three3000thousand') == 'Iloveyouthreethousand1143553000'
"""
def move_num(s):
    # Initialize an empty list to store non-numeric characters
    str_list = []
    
    # Iterate through each character in the input string
    for i in s:
        # Check if the character is not a digit
        if not i.isdigit():
            # Append non-digit characters to the list
            str_list.append(i)
    
    # Join the list into a string and return it
    return ''.join(str_list)

# Test the function with the provided test case
assert move_num('I1love143you55three3000thousand') == 'Iloveyouthreethousand1143553000'
