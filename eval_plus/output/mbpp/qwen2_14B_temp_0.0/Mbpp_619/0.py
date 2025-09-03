"""
Write a function to move all the numbers to the end of the given string.
assert move_num('I1love143you55three3000thousand') == 'Iloveyouthreethousand1143553000'
"""
import re

def move_num(s):
    # Extract digits and non-digit characters using regular expressions
    num = re.findall('\d+', s)
    alpha = re.findall('[a-zA-Z]+', s)
    
    # Join the lists of digits and non-digit characters
    result = ''.join(alpha) + ''.join(num)
    
    return result

# Test the function with the provided test case
assert move_num('I1love143you55three3000thousand') == 'Iloveyouthreethousand1143553000'
