
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
def add(lst):
    # Initialize sum to zero
    total = 0
    
    # Iterate over the list using enumerate to get both index and value
    for i, num in enumerate(lst):
        # Check if the index is odd and the number is even
        if i % 2 != 0 and num % 2 == 0:
            # Add the number to the total sum
            total += num
    
    # Return the computed sum
    return total

# Test cases to verify the correctness of the function
assert add([4, 2, 6, 7]) == 2
assert add([1, 3, 5, 7]) == 0
assert add([10, 22, 32, 43, 56]) == 22
assert add([0, 1, 2, 3, 4, 5, 6]) == 9