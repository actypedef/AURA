"""
Write a function to determine if the sum of the divisors of two integers are the same.
assert are_equivalent(36, 57) == False
"""
def are_equivalent(a, b):
    # Calculate the sum of divisors for each number
    def sum_of_divisors(n):
        return sum([i for i in range(1, n + 1) if n % i == 0])
    
    # Compare the sums of divisors of both numbers
    return sum_of_divisors(a) == sum_of_divisors(b)

# Test cases to verify the correctness of the function
assert are_equivalent(36, 57) == False
assert are_equivalent(48, 60) == True
assert are_equivalent(28, 35) == False
assert are_equivalent(100, 150) == True