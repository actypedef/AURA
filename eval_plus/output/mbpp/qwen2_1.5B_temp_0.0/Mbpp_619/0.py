"""
Write a function to move all the numbers to the end of the given string.
assert move_num('I1love143you55three3000thousand') == 'Iloveyouthreethousand1143553000'
"""
def move_num(s):
    # Split the string into parts based on digits
    parts = s.split('1')
    
    # Join the non-digit parts back together
    result = ''.join(parts)
    
    return result

# Test cases to verify the correctness of the solution
assert move_num('I1love143you55three3000thousand') == 'Iloveyouthreethousand1143553000'
assert move_num('Hello123World456') == 'HelloWorld456123'
assert move_num('NoNumbersHere') == 'NoNumbersHere'
assert move_num('1234567890') == '1234567890'
assert move_num('') == ''