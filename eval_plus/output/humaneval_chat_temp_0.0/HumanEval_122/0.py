
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
    
    :param arr: List[int] - A list of integers.
    :param k: int - The number of elements to consider from the start of the list.
    :return: int - The sum of elements with at most two digits from the first k elements.
    """
    # Initialize the sum to zero
    total_sum = 0
    
    # Iterate through the first k elements of the array
    for i in range(k):
        # Check if the current element has at most two digits
        if -99 <= arr[i] <= 99:
            # Add the element to the total sum
            total_sum += arr[i]
    
    # Return the computed sum
    return total_sum

# Test cases to verify the correctness of the function
assert add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 4) == 24
assert add_elements([10, 20, 30, 40, 50], 3) == 60
assert add_elements([-10, 200, 30, -40, 500], 5) == -10
assert add_elements([1, 2, 3, 4, 5], 1) == 1
assert add_elements([99, 100, 101, 98], 4) == 197
