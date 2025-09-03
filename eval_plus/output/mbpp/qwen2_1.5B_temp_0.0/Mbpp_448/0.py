"""
Write a function to calculate the sum of perrin numbers.
assert cal_sum(9) == 49
"""
def cal_sum(n):
    # Initialize the first three Perrin numbers
    p1, p2, p3 = 3, 0, 2
    
    # Calculate the sum of the first n Perrin numbers
    total_sum = 0
    for _ in range(n):
        total_sum += p1
        p1, p2, p3 = p2, p3, p1 + p2 + p3
    
    return total_sum

# Test cases to verify the correctness of the solution
assert cal_sum(9) == 49
assert cal_sum(5) == 7
assert cal_sum(6) == 18