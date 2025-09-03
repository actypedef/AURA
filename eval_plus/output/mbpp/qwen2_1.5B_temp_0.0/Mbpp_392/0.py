"""
Write a function to find the maximum sum possible by using the given equation f(n) = max( (f(n/2) + f(n/3) + f(n/4) + f(n/5)), n).
assert get_max_sum(60) == 106
"""
def get_max_sum(n):
    # Base case: if n is less than or equal to 5, return n itself
    if n <= 5:
        return n
    
    # Recursive case: calculate the maximum sum using the given equation
    return max(get_max_sum(n//2) + get_max_sum(n//3) + get_max_sum(n//4) + get_max_sum(n//5), n)

# Test cases to verify the correctness of the solution
assert get_max_sum(60) == 106
assert get_max_sum(70) == 118
assert get_max_sum(80) == 126
assert get_max_sum(90) == 138
assert get_max_sum(100) == 150