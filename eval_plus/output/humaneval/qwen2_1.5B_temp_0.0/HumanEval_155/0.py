
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
# Define the function to count even and odd digits in a given number
def even_odd_count(num):
    # Convert the number to its absolute value for easier handling
    num = abs(num)
    
    # Initialize counters for even and odd digits
    even_count = 0
    odd_count = 0
    
    # Iterate over each digit in the number
    while num > 0:
        digit = num % 10
        
        # Check if the digit is even or odd
        if digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        
        # Remove the last digit from the number
        num //= 10
    
    # Return the counts as a tuple
    return (even_count, odd_count)

# Test cases to verify the correctness of the function
assert even_odd_count(-12) == (1, 1), "Test case -12 failed"
assert even_odd_count(123) == (1, 2), "Test case 123 failed"
assert even_odd_count(0) == (1, 0), "Test case 0 failed"
assert even_odd_count(11111111111111111) == (1, 0), "Test case 11111111111111111 failed"
