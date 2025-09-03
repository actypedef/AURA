"""
Write a function to remove all the words with k length in the given string.
assert remove_length('The person is most value tet', 3) == 'person is most value'
"""
def remove_length(s, k):
    # Split the input string into a list of words
    s = s.split()
    
    # Filter out words whose length is equal to k
    s = [i for i in s if len(i) != k]
    
    # Join the filtered list back into a single string
    return " ".join(s)

# Test the function with the provided test case
assert remove_length('The person is most value tet', 3) == 'person is most value'
