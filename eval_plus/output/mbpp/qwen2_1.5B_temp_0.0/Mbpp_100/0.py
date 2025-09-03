"""
Write a function to find the next smallest palindrome of a specified integer, returned as an integer.
assert next_smallest_palindrome(99)==101
"""
def next_smallest_palindrome(n):
    # Convert the number to string to easily manipulate its digits
    str_n = str(n)
    
    # Find the length of the number
    len_n = len(str_n)
    
    # Check if the number is already a palindrome
    if str_n == str_n[::-1]:
        # If it's a palindrome, increment the last digit and check for palindromes again
        while True:
            n += 1
            str_n = str(n)
            if str_n == str_n[::-1]:
                return n
    
    # If the number is not a palindrome, find the next smallest palindrome
    else:
        # Find the middle index of the number
        mid_index = len_n // 2
        
        # If the number has an odd length, adjust the middle digit
        if len_n % 2 != 0:
            str_n = str_n[:mid_index] + str(int(str_n[mid_index]) + 1) + str_n[mid_index+1:]
        
        # If the number has an even length, adjust both halves
        else:
            str_n = str_n[:mid_index] + str(int(str_n[mid_index])) + str_n[mid_index]
            str_n = str_n[:mid_index] + str(int(str_n[mid_index]) + 1) + str_n[mid_index:]
        
        # Convert the modified string back to an integer
        return int(str_n)

# Test cases to verify the correctness of the function
assert next_smallest_palindrome(99) == 100
assert next_smallest_palindrome(123) == 131
assert next_smallest_palindrome(121) == 131
assert next_smallest_palindrome(123456789) == 123456791