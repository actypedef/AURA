
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
# Define the function to find the biggest even number in a given range
def choose_num(x, y):
    # Ensure both inputs are positive integers
    if not (isinstance(x, int) and isinstance(y, int)) or x <= 0 or y <= 0:
        raise ValueError("Both inputs must be positive integers.")
    
    # Find the smallest number in the range
    start = min(x, y)
    # Find the largest even number in the range
    end = max(start + 1, start + 2) if start % 2 == 0 else start
    
    # Return the largest even number if it exists; otherwise, return -1
    return end if end % 2 == 0 else -1

# Test cases to verify the correctness of the function
assert choose_num(12, 15) == 14
assert choose_num(13, 12) == -1
assert choose_num(8, 10) == 10
assert choose_num(7, 9) == -1