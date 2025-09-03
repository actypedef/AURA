

def is_prime(n):
    """Return true if a given number is prime, and false otherwise.
    >>> is_prime(6)
    False
    >>> is_prime(101)
    True
    >>> is_prime(11)
    True
    >>> is_prime(13441)
    True
    >>> is_prime(61)
    True
    >>> is_prime(4)
    False
    >>> is_prime(1)
    False
    """
# Define the function to check if a number is prime
def is_prime(n):
    """Return true if a given number is prime, and false otherwise."""
    # Check for edge cases
    if n <= 1:
        return False
    # Check for factors from 2 to the square root of n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Test cases to verify the correctness of the function
test_cases = [
    (6, False),
    (101, True),
    (11, True),
    (13441, True),
    (61, True),
    (4, False),
    (1, False)
]

# Function to run test cases and print results
def run_tests():
    for input_val, expected_output in test_cases:
        assert is_prime(input_val) == expected_output, f"Failed on {input_val}"
    print("All test cases passed!")

# Run the tests
run_tests()