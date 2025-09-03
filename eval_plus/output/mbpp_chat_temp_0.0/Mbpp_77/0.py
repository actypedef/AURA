"""
Write a python function to find whether a number is divisible by 11.
assert is_Diff (12345) == False
"""
def is_Diff(n):
    # Convert the number to a string to easily access each digit
    s = str(n)
    
    # Initialize variables to store the sum of digits at even and odd positions
    even_sum = 0
    odd_sum = 0
    
    # Iterate through the digits of the number
    for i in range(len(s)):
        if i % 2 == 0:
            # Add digit at even position to even_sum
            even_sum += int(s[i])
        else:
            # Add digit at odd position to odd_sum
            odd_sum += int(s[i])
    
    # Check if the difference between even_sum and odd_sum is divisible by 11
    return (even_sum - odd_sum) % 11 == 0

# Test the function with the provided test case
assert is_Diff(12345) == False