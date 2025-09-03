

def sum_to_n(n: int):
    """sum_to_n is a function that sums numbers from 1 to n.
    >>> sum_to_n(30)
    465
    >>> sum_to_n(100)
    5050
    >>> sum_to_n(5)
    15
    >>> sum_to_n(10)
    55
    >>> sum_to_n(1)
    1
    """
# Function to calculate the sum of numbers from 1 to n
def sum_to_n(n: int) -> int:
    # Using the formula for the sum of the first n natural numbers
    return n * (n + 1) // 2

# Example usage and testing