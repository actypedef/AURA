
def file_name_check(file_name):
    """Create a function which takes a string representing a file's name, and returns
    'Yes' if the the file's name is valid, and returns 'No' otherwise.
    A file's name is considered to be valid if and only if all the following conditions 
    are met:
    - There should not be more than three digits ('0'-'9') in the file's name.
    - The file's name contains exactly one dot '.'
    - The substring before the dot should not be empty, and it starts with a letter from 
    the latin alphapet ('a'-'z' and 'A'-'Z').
    - The substring after the dot should be one of these: ['txt', 'exe', 'dll']
    Examples:
    file_name_check("example.txt") # => 'Yes'
    file_name_check("1example.dll") # => 'No' (the name should start with a latin alphapet letter)
    """
import re

def file_name_check(file_name):
    """
    Create a function which takes a string representing a file's name, and returns
    'Yes' if the the file's name is valid, and returns 'No' otherwise.
    A file's name is considered to be valid if and only if all the following conditions 
    are met:
    - There should not be more than three digits ('0'-'9') in the file's name.
    - The file's name contains exactly one dot '.'
    - The substring before the dot should not be empty, and it starts with a letter from 
    the latin alphapet ('a'-'z' and 'A'-'Z').
    - The substring after the dot should be one of these: ['txt', 'exe', 'dll']
    Examples:
    file_name_check("example.txt") # => 'Yes'
    file_name_check("1example.dll") # => 'No' (the name should start with a latin alphapet letter)
    """
    # Check for exactly one dot
    if file_name.count('.') != 1:
        return 'No'
    
    # Split the file name into name and extension
    name, extension = file_name.split('.')
    
    # Check for valid extension
    if extension not in ['txt', 'exe', 'dll']:
        return 'No'
    
    # Check for valid name
    if not re.match('^[a-zA-Z][a-zA-Z0-9]*$', name):
        return 'No'
    
    # Check for no more than three digits
    if len(re.findall('\d', name)) > 3:
        return 'No'
    
    return 'Yes'

# Test cases
assert file_name_check("example.txt") == 'Yes'
assert file_name_check("1example.dll") == 'No'
assert file_name_check("example123.txt") == 'Yes'
assert file_name_check("example1234.txt") == 'No'
assert file_name_check("example.txt.") == 'No'
assert file_name_check("example.tx") == 'No'
assert file_name_check("example.exe") == 'Yes'
assert file_name_check("example.dll") == 'Yes'
assert file_name_check("example.doc") == 'No'
assert file_name_check("example.txt1") == 'No'
assert file_name_check("example.txt12") == 'No'
assert file_name_check("example.txt123") == 'No'
assert file_name_check("example.txt1234") == 'No'
assert file_name_check("example.txt12345") == 'No'
assert file_name_check("example.txt123456") == 'No'
assert file_name_check("example.txt1234567") == 'No'
assert file_name_check("example.txt12345678") == 'No'
assert file_name_check("example.txt123456789") == 'No'
assert file_name_check("example.txt1234567890") == 'No'
assert file_name_check("example.txt12345678901") == 'No'
assert file_name_check("example.txt123456789012") == 'No'
assert file_name_check("example.txt1234567890123") == 'No'
assert file_name_check("example.txt12345678901234") == 'No'
assert file_name_check("example.txt123456789012345