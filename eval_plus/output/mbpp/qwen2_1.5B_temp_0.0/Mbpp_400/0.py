"""
Write a function to extract the number of unique tuples in the given list.
assert extract_freq([(3, 4), (1, 2), (4, 3), (5, 6)] ) == 3
"""
def extract_freq(lst):
    # Convert each tuple to a set to remove duplicates
    unique_tuples = {tuple(item) for item in lst}
    # Return the count of unique tuples
    return len(unique_tuples)

# Test cases to verify the correctness of the solution
assert extract_freq([(3, 4), (1, 2), (4, 3), (5, 6)]) == 3
assert extract_freq([(10, 20), (20, 30), (30, 40), (40, 50)]) == 4
assert extract_freq([(1, 1), (2, 2), (3, 3), (4, 4)]) == 1
assert extract_freq([]) == 0