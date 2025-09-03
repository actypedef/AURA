"""
Write a function to check whether the given number is undulating or not.
assert is_undulating(1212121) == True
"""
def is_undulating(n):
    # Convert the number to a string for easy manipulation
    s = str(n)
    
    # Check if the length of the number is less than 3
    if len(s) < 3:
        return False
    
    # Extract the first two digits
    a, b = int(s[0]), int(s[1])
    
    # If the first two digits are the same, it's not undulating
    if a == b:
        return False
    
    # Iterate through the string starting from the third digit
    i = 2
    while i < len(s):
        # Check if the current digit matches the previous one
        if int(s[i]) != int(s[i - 1]):
            return False
        
        # Move to the next pair of digits
        i += 1
    
    # If all checks pass, the number is undulating
    return True

# Test the function with the provided test case
assert is_undulating(1212121) == True