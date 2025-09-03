"""
Write a function to check if the given number is woodball or not.
assert is_woodall(383) == True
"""
def is_woodall(n):
    # Check if n is less than 2
    if n < 2:
        return False
    
    # Initialize x as 1
    x = 1
    
    # Loop until x * (x + 1) is greater than or equal to n
    while x * (x + 1) <= n:
        # If x * (x + 1) equals n, return True
        if x * (x + 1) == n:
            return True
        
        # Increment x by 1
        x += 1
    
    # Return False if no match is found
    return False

# Test the function with the provided test case
assert is_woodall(383) == True