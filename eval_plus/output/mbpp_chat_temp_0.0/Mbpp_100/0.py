"""
Write a function to find the next smallest palindrome of a specified integer, returned as an integer.
assert next_smallest_palindrome(99)==101
"""
def next_smallest_palindrome(n):
    # Convert the number to a string to easily manipulate digits
    s = str(n)
    
    # If the number has only one digit or is already a palindrome, return the next number
    if len(s) == 1 or s == s[::-1]:
        return n + 1
    
    # Find the middle index of the number
    mid = len(s) // 2
    
    # Check if the left half of the number is greater than its reverse
    if s[:mid] > s[mid:][::-1]:
        # Increment the left half and mirror it to form a new palindrome
        return int(s[:mid] + s[:mid][::-1])
    
    # If the left half is not greater, increment the entire number and check again
    while True:
        n += 1
        s = str(n)
        if s == s[::-1]:
            return n

# Test the function with the provided test case
assert next_smallest_palindrome(99) == 101