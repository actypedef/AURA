
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
def choose_num(x, y):
    # Check if the range is valid (x <= y)
    if x > y:
        return -1
    
    # Start from the end of the range and move backwards to find the largest even number
    for num in range(y, x - 1, -1):
        if num % 2 == 0:  # Check if the number is even
            return num
    
    # Return -1 if no even number is found
    return -1

# Test cases to verify the correctness of the function