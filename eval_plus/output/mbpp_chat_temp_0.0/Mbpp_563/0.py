"""
Write a function to extract values between quotation marks from a string.
assert extract_values('"Python", "PHP", "Java"')==['Python', 'PHP', 'Java']
"""
def extract_values(string):
    # Split the input string by commas and strip whitespace
    words = string.split(',')
    
    # Initialize an empty list to store the extracted values
    result = []
    
    # Iterate over each word in the split list
    for word in words:
        # Strip leading and trailing whitespace
        word = word.strip()
        
        # Check if the word starts and ends with a double quote
        if word.startswith('"') and word.endswith('"'):
            # Remove the double quotes and append to the result list
            result.append(word[1:-1])
    
    return result

# Test the function with the provided test case
assert extract_values('"Python", "PHP", "Java"') == ['Python', 'PHP', 'Java']
