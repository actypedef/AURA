

def sum_squares(lst):
    """You are given a list of numbers.
    You need to return the sum of squared numbers in the given list,
    round each element in the list to the upper int(Ceiling) first.
    Examples:
    For lst = [1,2,3] the output should be 14
    For lst = [1,4,9] the output should be 98
    For lst = [1,3,5,7] the output should be 84
    For lst = [1.4,4.2,0] the output should be 29
    For lst = [-2.4,1,1] the output should be 6
    

    """
import math

def sum_squares(lst):
    # Round each number in the list to the nearest higher integer using ceiling
    rounded_list = [math.ceil(num) for num in lst]
    # Square each number in the rounded list
    squared_list = [num ** 2 for num in rounded_list]
    # Sum all the squared numbers
    total_sum = sum(squared_list)
    return total_sum

# Test cases to verify the correctness of the function
assert sum_squares([1,2,3]) == 14
assert sum_squares([1,4,9]) == 98
assert sum_squares([1,3,5,7]) == 84
assert sum_squares([1.4,4.2,0]) == 29
assert sum_squares([-2.4,1,1]) == 6