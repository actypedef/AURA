"""
Write a function to check if a string is present as a substring in a given list of string values.
assert find_substring(["red", "black", "white", "green", "orange"],"ack")==True
"""
def find_substring(list1, s):
    # Iterate through each element in the list
    for x in list1:
        # Check if the substring 's' is found in the current element
        if s in x:
            return True
    # Return False if the substring is not found in any element
    return False

# Test the function with the provided test case
assert find_substring(["red", "black", "white", "green", "orange"], "ack") == True