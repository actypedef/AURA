"""
Write a function to check if a string is present as a substring in a given list of string values.
assert find_substring(["red", "black", "white", "green", "orange"],"ack")==True
"""
def find_substring(string_list, target_string):
    # Check if the target string is present in any of the strings in the list
    return target_string in string_list

# Test cases to verify the correctness of the function
assert find_substring(["red", "black", "white", "green", "orange"], "ack") == True
assert find_substring(["apple", "banana", "cherry"], "date") == False
assert find_substring(["hello", "world", "python", "programming"], "python") == True
assert find_substring(["test", "case", "example"], "test") == True
assert find_substring(["one", "two", "three"], "four") == False