
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # Ensure a is less than or equal to b
    if a > b:
        a, b = b, a
    
    # Generate list of even numbers between a and b (inclusive)
    even_numbers = [x for x in range(a, b + 1) if x % 2 == 0]
    
    return even_numbers

# Check function to verify the correctness of the solution
def check_function():
    assert generate_integers(2, 8) == [2, 4, 6, 8], "Test case 1 failed"
    assert generate_integers(8, 2) == [2, 4, 6, 8], "Test case 2 failed"
    assert generate_integers(10, 14) == [], "Test case 3 failed"
    print("All test cases passed!")

# Run the check function to validate the solution
check_function()