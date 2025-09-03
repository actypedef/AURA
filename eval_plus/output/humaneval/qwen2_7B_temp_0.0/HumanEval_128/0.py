
def prod_signs(arr):
    """
    You are given an array arr of integers and you need to return
    sum of magnitudes of integers multiplied by product of all signs
    of each number in the array, represented by 1, -1 or 0.
    Note: return None for empty arr.

    Example:
    >>> prod_signs([1, 2, 2, -4]) == -9
    >>> prod_signs([0, 1]) == 0
    >>> prod_signs([]) == None
    """
def prod_signs(arr):
    if not arr:  # Check if the array is empty
        return None
    
    magnitude_sum = sum(abs(x) for x in arr)  # Sum of magnitudes
    sign_product = 1
    
    for num in arr:
        if num == 0:
            sign_product = 0  # If any number is zero, the product of signs will be zero
            break
        elif num < 0:
            sign_product *= -1  # Multiply by -1 for negative numbers
    
    return magnitude_sum * sign_product

# Test cases