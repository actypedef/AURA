"""
Write a function that takes in a list of tuples and returns a list containing the rear element of each tuple.
assert rear_extract([(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19)]) == [21, 20, 19]
"""
def rear_extract(tuples_list):
    # Extracting the last element from each tuple using list comprehension
    return [t[-1] for t in tuples_list]

# Test cases to verify the correctness of the solution
assert rear_extract([(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19)]) == [21, 20, 19]
assert rear_extract([(5, 'Alice', 35), (6, 'Bob', 40), (7, 'Charlie', 45)]) == [35, 40, 45]
assert rear_extract([(8, 'David', 50), (9, 'Eve', 55), (10, 'Frank', 60)]) == [50, 55, 60]