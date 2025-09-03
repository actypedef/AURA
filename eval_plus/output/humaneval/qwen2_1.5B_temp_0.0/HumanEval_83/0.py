
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
# Importing necessary packages
from typing import List

def starts_one_ends(n: int) -> int:
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 1:
        return 1  # Only one number (1 itself)
    
    # For n > 1, there are 2 options for each digit (either 1 or not 1)
    # Therefore, we have 2^(n-1) possible combinations
    return 2**(n-1)

# Function to check the correctness of the solution
def check_solution():
    test_cases = [
        (1, 1),  # Single digit number starting or ending with 1
        (2, 3),  # Two digits number starting or ending with 1
        (3, 7),  # Three digits number starting or ending with 1
        (4, 15)  # Four digits number starting or ending with 1
    ]
    
    for input_n, expected_output in test_cases:
        assert starts_one_ends(input_n) == expected_output, f"Test failed for input {input_n}. Expected {expected_output}, got {starts_one_ends(input_n)}"
    print("All test cases passed!")

# Running the check function to verify the solution
check_solution()