"""
Write a python function to find the sum of the per-digit difference between two integers.
assert digit_distance_nums(1,2) == 1
"""
def digit_distance_nums(n1, n2):
    # Convert numbers to strings and iterate over each digit
    return sum(int(abs(int(d1) - int(d2))) for d1, d2 in zip(str(n1), str(n2)))

# Test the function with the provided test case
assert digit_distance_nums(1, 2) == 1