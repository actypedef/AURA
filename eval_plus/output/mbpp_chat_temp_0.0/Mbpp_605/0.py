"""
Write a function to check if the given integer is a prime number.
assert prime_num(13)==True
"""
def prime_num(n):
    # Check if the number is less than 2
    if n <= 1:
        return False
    # Check for factors from 2 to the square root of n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Test the function with the provided test case
assert prime_num(13) == True