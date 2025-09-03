"""
Write a function to check if the given integer is a prime number.
assert prime_num(13)==True
"""
def prime_num(num):
    # Check if the number is less than 2
    if num < 2:
        return False
    # Check for factors from 2 to the square root of num
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Test the function with the provided test case
assert prime_num(13) == True
