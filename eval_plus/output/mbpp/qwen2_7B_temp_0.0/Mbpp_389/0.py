"""
Write a function to find the n'th lucas number.
assert find_lucas(9) == 76
"""
def find_lucas(n):
    # Base cases for the first two Lucas numbers
    if n == 0:
        return 2
    elif n == 1:
        return 1
    
    # Initialize the first two Lucas numbers
    lucas = [2, 1]
    
    # Calculate the nth Lucas number using a loop
    for i in range(2, n + 1):
        lucas.append(lucas[i - 1] + lucas[i - 2])
    
    # Return the nth Lucas number
    return lucas[n]

# Test the function with the provided test case
assert find_lucas(9) == 76