"""
Write a function to sum the length of the names of a given list of names after removing the names that start with a lowercase letter.
assert sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith'])==16
"""
def sample_nam(names):
    # Filter out names that start with a lowercase letter using a generator expression
    return sum(len(name) for name in names if not name[0].islower())

# Test the function with the provided test case
assert sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith']) == 16
