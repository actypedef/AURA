"""
Write a function to sum all amicable numbers from 1 to a specified number.
assert amicable_numbers_sum(999)==504
"""
def amicable_numbers_sum(n):
    def proper_divisors(num):
        return [i for i in range(1, num) if num % i == 0]

    def is_amicable(a, b):
        return sum(proper_divisors(a)) == b and sum(proper_divisors(b)) == a

    amicable_pairs = [(a, b) for a in range(1, n+1) for b in range(a+1, n+1) if is_amicable(a, b)]
    return sum(sum(pair) for pair in amicable_pairs)

# Test the function
assert amicable_numbers_sum(999) == 504