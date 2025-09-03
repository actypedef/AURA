"""
Write a function to check if a string is present as a substring in a given list of string values.
assert find_substring(["red", "black", "white", "green", "orange"],"ack")==True
"""
def find_substring(list1, sample):
    # Check if any string in the list contains the sample substring
    for i in list1:
        if sample in i:
            return True
    return False

# Test the function with the provided test case
assert find_substring(["red", "black", "white", "green", "orange"], "ack") == True
