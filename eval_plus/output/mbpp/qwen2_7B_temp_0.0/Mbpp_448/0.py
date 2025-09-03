"""
Write a function to calculate the sum of perrin numbers.
assert cal_sum(9) == 49
"""
def cal_sum(n):
    # Initialize the first three Perrin numbers
    p0 = 3
    p1 = 0
    p2 = 2
    
    # If n is less than or equal to 2, return the corresponding Perrin number
    if n <= 2:
        return p0 if n == 0 else (p0 + p1 if n == 1 else p2)
    
    # Calculate the sum of Perrin numbers up to n
    for i in range(3, n + 1):
        # Calculate the next Perrin number using the formula P(i) = P(i-2) + P(i-3)
        p_next = p0 + p1
        
        # Update the previous three Perrin numbers
        p0 = p1
        p1 = p2
        p2 = p_next
    
    # Return the sum of Perrin numbers up to n
    return p0

# Test the function with the provided test case
assert cal_sum(9) == 49
