"""
Write a python function to check if a given number is one less than twice its reverse.
assert check(70) == False
"""
def check(n):
    # Calculate the reverse of the number
    rev = 0
    temp = n
    
    while temp > 0:
        rem = temp % 10
        rev = (rev * 10) + rem
        temp //= 10
    
    # Check if the number is one less than twice its reverse
    return (2 * rev - 1 == n)

# Test the function with the provided test case
assert check(70) == False
