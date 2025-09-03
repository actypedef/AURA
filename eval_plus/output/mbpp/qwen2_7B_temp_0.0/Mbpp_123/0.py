"""
Write a function to sum all amicable numbers from 1 to a specified number.
assert amicable_numbers_sum(999)==504
"""
def amicable_numbers_sum(n):
    # Helper function to calculate the sum of divisors of a number
    def sum_of_divisors(num):
        total = 1
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                total += i
                if i != num // i:
                    total += num // i
        return total
    
    # Dictionary to store the sum of divisors for each number up to n
    divisor_sums = {i: sum_of_divisors(i) for i in range(1, n+1)}
    
    # Set to store amicable numbers
    amicable_set = set()
    
    # Find amicable numbers
    for i in range(1, n+1):
        j = divisor_sums[i]
        if i != j and divisor_sums[j] == i:
            amicable_set.add(i)
            amicable_set.add(j)
    
    # Return the sum of all unique amicable numbers
    return sum(amicable_set)

# Test the function with the provided test case
assert amicable_numbers_sum(999) == 504
