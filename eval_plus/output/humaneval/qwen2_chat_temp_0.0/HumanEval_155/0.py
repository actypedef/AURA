
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    # Convert the number to its absolute value and then to a string to iterate over each digit
    num_str = str(abs(num))
    
    # Initialize counters for even and odd digits
    even_count = 0
    odd_count = 0
    
    # Iterate over each character in the string representation of the number
    for char in num_str:
        # Check if the digit is even or odd and update the respective counter
        if int(char) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    
    # Return the counts as a tuple
    return (even_count, odd_count)

# Test cases to verify the correctness of the function
assert even_odd_count(-12) == (1, 1), "Test case -12 failed"
assert even_odd_count(123) == (1, 2), "Test case 123 failed"
assert even_odd_count(0) == (1, 0), "Test case 0 failed"
assert even_odd_count(111) == (0, 3), "Test case 111 failed"
assert even_odd_count(2468) == (4, 0), "Test case 2468 failed"