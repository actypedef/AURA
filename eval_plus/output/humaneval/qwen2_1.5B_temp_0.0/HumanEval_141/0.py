
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
    # Check for more than three digits
    if len(re.findall(r'\d', file_name)) > 3:
        return "No"
    
    # Check for exactly one dot
    if '.' not in file_name:
        return "No"
    
    # Split the file name into two parts: before and after the dot
    parts = file_name.split('.')
    
    # Check if the first part is empty or does not start with a letter
    if len(parts[0]) == 0 or not parts[0][0].isalpha():
        return "No"
    
    # Check if the second part is one of the allowed extensions
    if parts[1] not in ['txt', 'exe', 'dll']:
        return "No"
    
    return "Yes"

# Test cases