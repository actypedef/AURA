
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
    
    # Initialize an empty list to store even digits
    even_digits = []
    
    # Iterate through each digit from a to b (inclusive)
    for num in range(a, b + 1):
        # Convert number to string to easily iterate over its digits
        str_num = str(num)
        
        # Check each character if it's even
        for char in str_num:
            if int(char) % 2 == 0:
                # Append even digit to the list
                even_digits.append(int(char))
    
    # Return the sorted list of even digits
    return sorted(even_digits)

# Test cases
assert generate_integers(2, 8) == [2, 4, 6, 8], "Test case 1 failed"
assert generate_integers(8, 2) == [2, 4, 6, 8], "Test case 2 failed"
assert generate_integers(10, 14) == [], "Test case 3 failed"