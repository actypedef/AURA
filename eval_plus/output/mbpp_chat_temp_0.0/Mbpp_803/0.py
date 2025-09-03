"""
Write a function to check whether the given number is a perfect square or not. https://www.geeksforgeeks.org/check-if-given-number-is-perfect-square-in-cpp/
assert not is_perfect_square(10)
"""
def is_perfect_square(n):
    # Check if the input number is less than 0
    if n < 0:
        return False
    
    # Initialize variables for binary search
    start = 0
    end = n
    
    # Perform binary search to find the square root of 'n'
    while start <= end:
        mid = (start + end) // 2
        
        # If the middle element squared equals 'n', it's a perfect square
        if mid * mid == n:
            return True
        # If the middle element squared is greater than 'n', adjust the upper bound
        elif mid * mid > n:
            end = mid - 1
        # If the middle element squared is less than 'n', adjust the lower bound
        else:
            start = mid + 1
    
    # If no perfect square is found, return False
    return False

# Test the function with the provided test case
assert not is_perfect_square(10)