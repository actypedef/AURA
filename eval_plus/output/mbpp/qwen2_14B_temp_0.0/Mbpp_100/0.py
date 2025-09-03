"""
Write a function to find the next smallest palindrome of a specified integer, returned as an integer.
assert next_smallest_palindrome(99)==101
"""
def next_smallest_palindrome(n):
    # Increment the number to find the next palindrome
    n += 1
    
    # Loop until a palindrome is found
    while True:
        # Check if the number is a palindrome
        if str(n) == str(n)[::-1]:
            return n
        n += 1

# Test the function with the provided test case
assert next_smallest_palindrome(99) == 101
