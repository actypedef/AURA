
def add_elements(arr, k):
    """
    Given a non-empty array of integers arr and an integer k, return
    the sum of the elements with at most two digits from the first k elements of arr.

    Example:

        Input: arr = [111,21,3,4000,5,6,7,8,9], k = 4
        Output: 24 # sum of 21 + 3

    Constraints:
        1. 1 <= len(arr) <= 100
        2. 1 <= k <= len(arr)
    """
def add_elements(arr, k):
    """
    Given a non-empty array of integers arr and an integer k, return
    the sum of the elements with at most two digits from the first k elements of arr.

    Example:

        Input: arr = [111,21,3,4000,5,6,7,8,9], k = 4
        Output: 24 # sum of 21 + 3

    Constraints:
        1. 1 <= len(arr) <= 100
        2. 1 <= k <= len(arr)
    """
    return sum([x for x in arr[:k] if -99 <= x <= 99])

# Test cases
assert add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 4) == 24
assert add_elements([10, 20, 30, 40, 50], 3) == 60
assert add_elements([100, 200, 300, 400, 500], 5) == 0
assert add_elements([1, 2, 3, 4, 5], 5) == 15
assert add_elements([10, 20, 30, 40, 50], 0) == 0
assert add_elements([10, 20, 30, 40, 50], 1) == 10
assert add_elements([10, 20, 30, 40, 50], 2) == 30
assert add_elements([10, 20, 30, 40, 50], 3) == 60
assert add_elements([10, 20, 30, 40, 50], 4) == 100
assert add_elements([10, 20, 30, 40, 50], 5) == 150