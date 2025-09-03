
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices.

    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    return sum(x for i, x in enumerate(lst) if i % 2 != 0 and x % 2 == 0)

# Test cases to verify the correctness of the function
assert add([4, 2, 6, 7]) == 2
assert add([1, 3, 5, 7]) == 0
assert add([2, 4, 6, 8]) == 4
assert add([10, 20, 30, 40, 50]) == 20
