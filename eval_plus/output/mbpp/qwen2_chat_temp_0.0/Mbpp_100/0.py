"""
Write a function to find the next smallest palindrome of a specified integer, returned as an integer.
assert next_smallest_palindrome(99)==101
"""
def next_smallest_palindrome(num):
    # Convert the number to a string to easily check for palindromes
    num_str = str(num)
    
    # Loop through numbers starting from one more than the given number
    for i in range(num + 1, 10**6):  # Limiting to 1 million to avoid infinite loop for large numbers
        if str(i) == str(i)[::-1]:  # Check if the number is a palindrome
            return i

# Test the function with the provided test case
assert next_smallest_palindrome(99) == 101