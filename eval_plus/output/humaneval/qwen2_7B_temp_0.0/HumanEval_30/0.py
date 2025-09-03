

def get_positive(l: list):
    """Return only positive numbers in the list.
    >>> get_positive([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    """
# Define the function to filter positive numbers from a list
def get_positive(l: list) -> list:
    # Use list comprehension to filter out non-positive numbers
    return [x for x in l if x > 0]

# Example usage of the function