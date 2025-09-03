"""
Write a function to check whether the given number is undulating or not.
assert is_undulating(1212121) == True
"""
def is_undulating(n):
    # Convert the number to string for easy manipulation
    num_str = str(n)
    
    # Check if the length of the number is less than 3
    if len(num_str) < 3:
        return False
    
    # Iterate through the digits of the number starting from the second digit
    for i in range(1, len(num_str)):
        # If the current digit is different from the previous one,
        # and either the next digit is greater than the current one
        # or the previous digit is greater than the next one,
        # then the number is not undulating
        if (num_str[i] != num_str[i-1]) and ((num_str[i] > num_str[i-1]) != (num_str[i] > num_str[i+1])):
            return False
    
    # If all conditions are met, the number is undulating
    return True

# Test cases to verify the correctness of the function
assert is_undulating(1212121) == True
assert is_undulating(1234567890) == False
assert is_undulating(1111111) == True
assert is_undulating(123456789) == False
assert is_undulating(12345678901234567890) == True
assert is_undulating(123456789012345678901234567890) == True
assert is_undulating(123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234