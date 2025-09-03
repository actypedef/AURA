"""
Write a function to find the n'th star number.
assert find_star_num(3) == 37
"""
def find_star_num(n):
    # Calculate the nth star number using the formula: n * (n + 1) / 2
    return int(n * (n + 1) / 2)

# Test the function with the provided test case
assert find_star_num(3) == 37
