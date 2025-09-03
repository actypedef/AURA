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
    for i in range(3, n):
        next_p = p0 + p1 + p2
        total += next_p
        p0, p1, p2 = p1, p2, next_p
    
    return total

# Test the function with the provided test case
assert cal_sum(9) == 49