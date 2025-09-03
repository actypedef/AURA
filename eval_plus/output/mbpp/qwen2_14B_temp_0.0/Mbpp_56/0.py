"""
Write a python function to check if a given number is one less than twice its reverse.
assert check(70) == False
"""
def check(n):
    # Calculate twice the reverse of the number
    twice_reverse = 2 * int(str(n)[::-1])
    
    # Check if the original number is one less than twice its reverse
    return n + 1 == twice_reverse

# Test the function with the provided test case
assert check(70) == False