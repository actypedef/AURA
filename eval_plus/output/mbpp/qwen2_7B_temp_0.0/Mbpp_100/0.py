"""
Write a function to find the next smallest palindrome of a specified integer, returned as an integer.
assert next_smallest_palindrome(99)==101
"""
def next_smallest_palindrome(n):
    # Increment the number to ensure we start checking from the next number
    n += 1
    
    # Convert the number to a string to check for palindrome property
    while str(n) != str(n)[::-1]:
        n += 1
    
    return n

# Test the function with the provided test case
assert next_smallest_palindrome(99) == 101
