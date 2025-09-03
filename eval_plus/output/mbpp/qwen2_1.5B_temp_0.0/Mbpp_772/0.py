"""
Write a function to remove all the words with k length in the given string.
assert remove_length('The person is most value tet', 3) == 'person is most value'
"""
def remove_length(s, k):
    # Split the string into words
    words = s.split()
    
    # Filter out words with length equal to k
    filtered_words = [word for word in words if len(word) != k]
    
    # Join the filtered words back into a single string
    result = ' '.join(filtered_words)
    
    return result

# Test cases
assert remove_length('The person is most value tet', 3) == 'person is most value'
assert remove_length('Hello world from Python', 4) == 'Hello world Python'
assert remove_length('Keep coding every day', 5) == 'Keep coding every day'