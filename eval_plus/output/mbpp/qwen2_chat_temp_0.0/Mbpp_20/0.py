"""
Write a function to check if the given number is woodball or not.
assert is_woodall(383) == True
"""
def is_woodall(n):
    # Check if n is less than 2
    if (n < 2):
        return False
    
    # Initialize variables for the loop
    k = 0
    x = 1
    
    # Loop until x becomes greater than or equal to n
    while (x < n):
        # Update x using the Woodall number formula
        x = 2 * x + 1
        
        # Increment k
        k += 1
    
    # Return True if x equals n, otherwise False
    return (x == n)

# Test the function with the provided test case
assert is_woodall(383) == True
