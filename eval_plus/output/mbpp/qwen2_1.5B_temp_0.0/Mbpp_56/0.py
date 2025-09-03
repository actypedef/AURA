"""
Write a python function to check if a given number is one less than twice its reverse.
assert check(70) == False
"""
def check(n):
    # Convert the number to a string to easily reverse it
    num_str = str(n)
    # Reverse the string
    reversed_num_str = num_str[::-1]
    # Convert the reversed string back to an integer
    reversed_num = int(reversed_num_str)
    # Check if the original number minus 1 is equal to twice the reversed number
    return (n - 1) == 2 * reversed_num

# Test cases
assert check(70) == False