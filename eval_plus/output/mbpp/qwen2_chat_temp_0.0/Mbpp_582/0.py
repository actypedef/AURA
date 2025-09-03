"""
Write a function to check if a dictionary is empty
assert my_dict({10})==False
"""
def my_dict(dict):
    # Check if the dictionary is empty using the len() function
    return not bool(len(dict))

# Test the function with the provided test case
assert my_dict({10}) == False
