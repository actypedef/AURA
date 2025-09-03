"""
Write a function to extract values between quotation marks from a string.
assert extract_values('"Python", "PHP", "Java"')==['Python', 'PHP', 'Java']
"""
def extract_values(string):
    # Split the input string by commas and then strip any leading/trailing whitespace or quotes
    return [i.strip(' ,').strip("'\"") for i in string.split(',')]

# Test the function with the provided test case
assert extract_values('"Python", "PHP", "Java"') == ['Python', 'PHP', 'Java']
