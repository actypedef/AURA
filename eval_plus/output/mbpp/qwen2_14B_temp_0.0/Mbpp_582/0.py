"""
Write a function to check if a dictionary is empty
assert my_dict({10})==False
"""
def my_dict(dict1):
    # Check if the dictionary is empty
    if not bool(dict1):
        return True
    else:
        return False

# Test the function with the provided test case
assert my_dict({10}) == False
