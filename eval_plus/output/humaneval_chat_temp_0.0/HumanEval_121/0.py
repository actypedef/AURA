
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
def solution(lst):
    # Initialize the sum to zero
    total_sum = 0
    
    # Iterate over the list using enumerate to get both index and value
    for index, value in enumerate(lst):
        # Check if the position (index) is even and the value is odd
        if index % 2 == 0 and value % 2 != 0:
            # Add the odd value to the total sum
            total_sum += value
    
    # Return the computed sum
    return total_sum

# Test cases to verify the correctness of the function
assert solution([5, 8, 7, 1]) == 12, "Test case 1 failed"
assert solution([3, 3, 3, 3, 3]) == 9, "Test case 2 failed"
assert solution([30, 13, 24, 321]) == 0, "Test case 3 failed"
