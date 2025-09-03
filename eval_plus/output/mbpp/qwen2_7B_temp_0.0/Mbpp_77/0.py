"""
Write a python function to find whether a number is divisible by 11.
assert is_Diff (12345) == False
"""
def is_Diff(n):
    # Convert the number to a string to easily access each digit
    s = str(n)
    
    # Calculate the difference between the sum of digits at odd positions and even positions
    diff = 0
    for i in range(len(s)):
        if i % 2 == 0:
            diff += int(s[i])
        else:
            diff -= int(s[i])
    
    # Check if the difference is divisible by 11
    return diff % 11 == 0

# Test the function with the provided test case
assert is_Diff(12345) == False