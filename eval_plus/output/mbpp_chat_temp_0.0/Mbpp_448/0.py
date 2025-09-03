"""
Write a function to calculate the sum of perrin numbers.
assert cal_sum(9) == 49
"""
def cal_sum(n):
    # Initialize the first three Perrin numbers
    p0 = 3
    p1 = 0
    p2 = 2
    
    # Base cases for n < 3
    if n == 0:
        return p0
    elif n == 1:
        return p0 + p1
    elif n == 2:
        return p0 + p1 + p2
    
    # Calculate the sum of Perrin numbers up to n
    total = p0 + p1 + p2
    for i in range(3, n + 1):
        # The next Perrin number is the sum of the two preceding ones
        p_next = p0 + p1
        total += p_next
        
        # Update the values for the next iteration
        p0 = p1
        p1 = p2
        p2 = p_next
    
    return total

# Test the function with the provided test case
assert cal_sum(9) == 49