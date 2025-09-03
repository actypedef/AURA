
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    
    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==> 0
    """
    # Initialize the sum to zero
    total_sum = 0
    
    # Iterate over the list using enumerate to get both index and value
    for i, num in enumerate(lst):
        # Check if the index is even and the number is odd
        if i % 2 == 0 and num % 2 != 0:
            # Add the number to the total sum
            total_sum += num
    
    # Return the final sum
    return total_sum

# Test cases