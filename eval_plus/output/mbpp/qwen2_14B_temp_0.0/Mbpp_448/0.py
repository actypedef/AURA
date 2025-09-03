"""
Write a function to calculate the sum of perrin numbers.
assert cal_sum(9) == 49
"""
def cal_sum(n):
    # Initialize the first three Perrin numbers
    p0, p1, p2 = 3, 0, 2
    
    # If n is 0, return the first Perrin number
    if n == 0:
        return p0
    
    # If n is 1, return the sum of the first two Perrin numbers
    if n == 1:
        return p0 + p1
    
    # If n is 2, return the sum of the first three Perrin numbers
    if n == 2:
        return p0 + p1 + p2
    
    # Initialize the sum with the first three Perrin numbers
    sm = p0 + p1 + p2
    
    # Calculate the sum of Perrin numbers up to the nth number
    for i in range(3, n + 1):
        # Calculate the next Perrin number
        p = p1 + p2
        
        # Update the sum
        sm += p
        
        # Update the previous Perrin numbers
        p0, p1, p2 = p1, p2, p
    
    # Return the final sum
    return sm

# Test the function with the provided test case
assert cal_sum(9) == 49
