"""
Write a python function to find the length of the longest word.
assert len_log(["python","PHP","bigdata"]) == 7
"""
def len_log(word_list):
    # Initialize maximum length to 0
    max_length = 0
    
    # Iterate through each word in the list
    for word in word_list:
        # Update max_length if the current word is longer
        if len(word) > max_length:
            max_length = len(word)
    
    return max_length

# Test the function with the provided test case
assert len_log(["python", "PHP", "bigdata"]) == 7
