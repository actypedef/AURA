"""
Write a function to return the sum of all divisors of a number.
assert sum_div(8)==7
"""
def sum_div(n):
    # Initialize sum with 1 because 1 is a divisor of every number
    sum = 1
    
    # Iterate from 2 to the square root of n
    for i in range(2, int(n**0.5) + 1):
        # If i is a divisor of n
        if n % i == 0:
            # Add i and its corresponding divisor n//i to the sum
            sum += i + n // i
    
    # If n is a perfect square, subtract the square root once
    if int(n**0.5)**2 == n:
        sum -= int(n**0.5)
    
    return sum

# Test the function with the provided test case
assert sum_div(8) == 7
