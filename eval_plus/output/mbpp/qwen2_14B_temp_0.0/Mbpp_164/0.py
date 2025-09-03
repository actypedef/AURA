"""
Write a function to determine if the sum of the divisors of two integers are the same.
assert are_equivalent(36, 57) == False
"""
def get_sum(n):
    # Initialize sum of divisors
    sum = 0
    
    # Iterate through all numbers from 1 to n
    for i in range(1, n + 1):
        if n % i == 0:
            sum += i
            
    return sum

def are_equivalent(num1, num2):
    # Compare the sum of divisors of both numbers
    return get_sum(num1) == get_sum(num2)

# Test the function with the provided test case
assert are_equivalent(36, 57) == False