"""
Write a python function to find the sum of fourth power of first n odd natural numbers.
assert odd_num_sum(2) == 82
"""
def odd_num_sum(n):
    sm = 0
    for i in range(0, n):
        # Calculate the (2*i + 1)th odd number and raise it to the fourth power
        sm = sm + ((2 * i + 1) ** 4)
    return sm

# Test the function with the provided test case
assert odd_num_sum(2) == 82
