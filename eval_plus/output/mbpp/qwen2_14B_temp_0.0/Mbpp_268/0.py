"""
Write a function to find the n'th star number.
assert find_star_num(3) == 37
"""
def find_star_num(n):
    # Calculate the n'th star number using the formula
    star_num = 6 * n * (n - 1) + 1
    return star_num

# Test the function with the provided test case
assert find_star_num(3) == 37
