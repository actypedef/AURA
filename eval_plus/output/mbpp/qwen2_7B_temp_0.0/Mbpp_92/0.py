"""
Write a function to check whether the given number is undulating or not.
assert is_undulating(1212121) == True
"""
def is_undulating(n):
    # Convert the number to a string to easily access individual digits
    s = str(n)
    
    # Check if the length of the string is less than 3, as undulation requires at least three digits
    if len(s) < 3:
        return False
    
    # Iterate through the string to check for undulation pattern
    for i in range(2, len(s)):
        # If any digit does not match the previous two digits, it's not undulating
        if s[i] != s[i - 2]:
            return False
    
    # If all checks pass, the number is undulating
    return True

# Test the function with the provided test case
assert is_undulating(1212121) == True
