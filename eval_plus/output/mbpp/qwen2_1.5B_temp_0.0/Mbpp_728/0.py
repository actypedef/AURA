"""
Write a function takes as input two lists [a_1,...,a_n], [b_1,...,b_n] and returns [a_1+b_1,...,a_n+b_n].
assert sum_list([10,20,30],[15,25,35])==[25,45,65]
"""
def sum_list(a, b):
    return [x + y for x, y in zip(a, b)]

# Test cases to verify the correctness of the solution
assert sum_list([10, 20, 30], [15, 25, 35]) == [25, 45, 65]
assert sum_list([1, 2, 3], [4, 5, 6]) == [5, 7, 9]
assert sum_list([-1, -2, -3], [-4, -5, -6]) == [-5, -7, -9]