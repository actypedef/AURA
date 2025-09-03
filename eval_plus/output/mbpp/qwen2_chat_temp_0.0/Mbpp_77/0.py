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
    
    # Iterate over each character in the string representation of the number
    for i in range(len(s)):
        # Check if the current position is even or odd
        if i % 2 == 0:
            # Add the digit to the even_sum
            even_sum += int(s[i])
        else:
            # Subtract the digit from the odd_sum
            odd_sum -= int(s[i])
    
    # Check if the difference between even_sum and odd_sum is divisible by 11
    return (even_sum - odd_sum) % 11 == 0

# Test the function with the provided test case
assert is_Diff(12345) == False