"""
Write a function to sum the length of the names of a given list of names after removing the names that start with a lowercase letter.
assert sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith'])==16
"""
def sample_nam(names):
    # Filter out names that start with a lowercase letter using a lambda function
    result = filter(lambda x: x[0].isupper(), names)
    # Sum the lengths of the remaining names
    return sum(len(x) for x in result)

# Test the function with the provided test case
assert sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith']) == 16
