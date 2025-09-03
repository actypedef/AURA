
def double_the_difference(lst):
    '''
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    
    double_the_difference([1, 3, 2, 0]) == 1 + 9 + 0 + 0 = 10
    double_the_difference([-1, -2, 0]) == 0
    double_the_difference([9, -2]) == 81
    double_the_difference([0]) == 0  
   
    If the input list is empty, return 0.
    '''
def double_the_difference(lst):
    """
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.

    Examples:
    double_the_difference([1, 3, 2, 0]) should return 10
    double_the_difference([-1, -2, 0]) should return 0
    double_the_difference([9, -2]) should return 81
    double_the_difference([0]) should return 0

    If the input list is empty, return 0.
    """
    # Filter out non-integer and negative numbers, then square the remaining odd numbers
    squared_odds = [x**2 for x in lst if isinstance(x, int) and x >= 0 and x % 2 != 0]
    # Return the sum of the squared odd numbers
    return sum(squared_odds)

# Check function to verify the correctness of the solution
def check():
    assert double_the_difference([1, 3, 2, 0]) == 10
    assert double_the_difference([-1, -2, 0]) == 0
    assert double_the_difference([9, -2]) == 81
    assert double_the_difference([0]) == 0
    assert double_the_difference([]) == 0
    print("All test cases pass.")

check()