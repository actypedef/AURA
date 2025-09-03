"""
Write a function to determine if the sum of the divisors of two integers are the same.
assert are_equivalent(36, 57) == False
"""
def are_equivalent(x, y):
    # Helper function to calculate the sum of divisors of a number
    def sum_of_divisors(n):
        total = 0
        for i in range(1, n + 1):
            if n % i == 0:
                total += i
        return total
    
    # Calculate the sum of divisors for both numbers
    sum_x = sum_of_divisors(x)
    sum_y = sum_of_divisors(y)
    
    # Compare the sums and return True if they are equal, False otherwise
    return sum_x == sum_y

# Test the function with the provided test case
assert are_equivalent(36, 57) == False