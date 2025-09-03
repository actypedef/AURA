

def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """
# Define the function below_threshold
def below_threshold(l: list, t: int):
    # Check if all elements in the list are less than or equal to the threshold
    return all(x <= t for x in l)

# Test cases to verify the correctness of the function
assert below_threshold([1, 2, 4, 10], 100) == True
assert below_threshold([1, 20, 4, 10], 5) == False

# Print the result of the test cases