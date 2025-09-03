

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
def median(l: list):
    """Return median of elements in the list l."""
    sorted_list = sorted(l)
    n = len(sorted_list)
    if n % 2 == 0:
        return (sorted_list[n // 2 - 1] + sorted_list[n // 2]) / 2
    else:
        return sorted_list[n // 2]

# Test cases