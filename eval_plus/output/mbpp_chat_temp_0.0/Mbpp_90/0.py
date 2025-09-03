"""
Write a python function to find the length of the longest word.
assert len_log(["python","PHP","bigdata"]) == 7
"""
def len_log(words):
    # Use the max function with key=len to find the longest word
    return len(max(words, key=len))

# Test the function with the provided test case
assert len_log(["python", "PHP", "bigdata"]) == 7
