"""
Write a function to remove all the words with k length in the given string.
assert remove_length('The person is most value tet', 3) == 'person is most value'
"""
def remove_length(s, k):
    # Split the input string into individual words
    words = s.split()
    
    # Filter out words that have exactly 'k' length
    filtered_words = [word for word in words if len(word) != k]
    
    # Join the remaining words back into a single string
    return ' '.join(filtered_words)

# Test the function with the provided test case
assert remove_length('The person is most value tet', 3) == 'person is most value'
