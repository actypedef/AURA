"""
Write a python function to find the length of the longest word.
assert len_log(["python","PHP","bigdata"]) == 7
"""
def len_log(words):
    # Initialize the maximum length variable to 0
    max_length = 0
    
    # Iterate through each word in the list
    for word in words:
        # Update the maximum length if the current word's length is greater
        if len(word) > max_length:
            max_length = len(word)
    
    # Return the maximum length found
    return max_length

# Test the function with the provided test case
assert len_log(["python", "PHP", "bigdata"]) == 7