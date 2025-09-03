
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
    Generate even numbers between two given integers a and b.
    
    Args:
    a (int): The starting integer.
    b (int): The ending integer.
    
    Returns:
    list: A list of even numbers between a and b in ascending order.
    """
    # Ensure a is less than or equal to b for correct iteration
    if a > b:
        a, b = b, a
    
    # Initialize an empty list to store even numbers
    even_numbers = []
    
    # Iterate through the range from a to b (inclusive)
    for num in range(a, b + 1):
        # Check if the number is even
        if num % 2 == 0:
            even_numbers.append(num)
    
    return even_numbers

# Example usage