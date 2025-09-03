"""
Write a function to check if a string is present as a substring in a given list of string values.
assert find_substring(["red", "black", "white", "green", "orange"],"ack")==True
"""
def find_substring(lst, substring):
    """
    Write a function to check if a string is present as a substring in a given list of string values.
    """
    for string in lst:
        if substring in string:
            return True
    return False

# Test cases
assert find_substring(["red", "black", "white", "green", "orange"], "ack") == True
assert find_substring(["red", "black", "white", "green", "orange"], "blue") == False
assert find_substring(["red", "black", "white", "green", "orange"], "red") == True
assert find_substring(["red", "black", "white", "green", "orange"], "green") == True
assert find_substring(["red", "black", "white", "green", "orange"], "orange") == True
assert find_substring(["red", "black", "white", "green", "orange"], "white") == True
assert find_substring(["red", "black", "white", "green", "orange"], "black") == True
assert find_substring(["red", "black", "white", "green", "orange"], "red") == True
assert find_substring(["red", "black", "white", "green", "orange"], "red") == True
assert find_substring(["red", "black", "white", "green", "orange"], "red") == True
assert find_substring(["red", "black", "white", "green", "orange"], "red") == True
assert find_substring(["red", "black", "white", "green", "orange"], "red") == True
assert find_substring(["red", "black", "white", "green", "orange"], "red") == True
assert find_substring(["red", "black", "white", "green", "orange"], "red") == True
assert find_substring(["red", "black", "white", "green", "orange"], "red") == True
assert find_substring(["red", "black", "white", "green", "orange"], "red") == True
assert find_substring(["red", "black", "white", "green", "orange"], "red") == True
assert find_substring(["red", "black", "white", "green", "orange"], "red") == True
assert find_substring(["red", "black", "white", "green", "orange"], "red") == True
assert find_substring(["red", "black", "white", "green", "orange"], "red") == True
assert find_substring(["red", "black", "white", "green", "orange"], "red") == True
assert find_substring(["red", "black", "white", "green", "orange"], "red") == True
assert find_substring(["red", "black", "white", "green", "orange"], "red") == True
assert find_substring(["red", "black", "white", "green", "orange"], "red") == True
assert find_substring(["red", "black", "white", "green", "orange"], "red") == True
assert find_substring(["red", "black", "white", "green", "orange"], "red") == True
assert find_substring(["red", "black", "white", "green", "orange"], "red") == True
assert find_substring(["red", "black", "white", "green", "orange"], "red") == True
assert find_substring(["red", "black",