"""
Write a function to extract values between quotation marks from a string.
assert extract_values('"Python", "PHP", "Java"')==['Python', 'PHP', 'Java']
"""
def extract_values(s):
    # Split the input string by commas and remove any leading or trailing quotes
    return [value.strip('"') for value in s.split(',')]

# Test cases to verify the correctness of the function
assert extract_values('"Python", "PHP", "Java"')==['Python', 'PHP', 'Java']
assert extract_values('"JavaScript", "C++", "Ruby"')==['JavaScript', 'C++', 'Ruby']
assert extract_values('"HTML", "CSS", "SQL"')==['HTML', 'CSS', 'SQL']