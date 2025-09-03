"""
Write a function to check if a string is present as a substring in a given list of string values.
assert find_substring(["red", "black", "white", "green", "orange"],"ack")==True
"""
def find_substring(list1, s):
    # Check if any element in the list contains the substring 's'
    return any(s in x for x in list1)

# Test the function with the provided test case
assert find_substring(["red", "black", "white", "green", "orange"], "ack") == True
