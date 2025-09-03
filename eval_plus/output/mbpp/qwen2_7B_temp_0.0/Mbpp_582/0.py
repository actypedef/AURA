"""
Write a function to check if a dictionary is empty
assert my_dict({10})==False
"""
# Define a function to check if a dictionary is empty
def my_dict(dict):
    # Check if the length of the dictionary is 0
    return len(dict) == 0

# Test the function with a non-empty dictionary
assert my_dict({10}) == False
