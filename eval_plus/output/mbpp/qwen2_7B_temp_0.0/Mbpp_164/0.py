"""
Write a function to determine if the sum of the divisors of two integers are the same.
assert are_equivalent(36, 57) == False
"""
def are_equivalent(n1, n2):
    # Helper function to calculate the sum of divisors of a number
    def divisor_sum(num):
        total = 0
        for i in range(1, num + 1):
            if num % i == 0:
                total += i
        return total
    
    # Calculate the sum of divisors for both numbers
    sum_n1 = divisor_sum(n1)
    sum_n2 = divisor_sum(n2)
    
    # Compare the sums of divisors
    return sum_n1 == sum_n2

# Test the function with the provided test case
assert are_equivalent(36, 57) == False
