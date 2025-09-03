"""
Write a python function to check if a given number is one less than twice its reverse.
assert check(70) == False
"""
def reverse(n):
    # Initialize variables to store the reversed number and the remainder
    rev = 0
    rem = 0
    
    # Loop until n becomes 0
    while n != 0:
        rem = n % 10  # Get the last digit of n
        rev = (rev * 10) + rem  # Append the last digit to rev
        n = n // 10  # Remove the last digit from n
    
    return rev

def check(n):
    # Check if the number is one less than twice its reverse
    return n == 2 * reverse(n) - 1

# Test the function with the provided test case
assert check(70) == False
