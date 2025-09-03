"""
Write a function to find minimum k records from tuple list. https://www.geeksforgeeks.org/python-find-minimum-k-records-from-tuple-list/ - in this case a verbatim copy of test cases
assert min_k([('Manjeet', 10), ('Akshat', 4), ('Akash', 2), ('Nikhil', 8)], 2) == [('Akash', 2), ('Akshat', 4)]
"""
def min_k(tuples_list, k):
    # Sort the tuples based on their second element (value)
    sorted_tuples = sorted(tuples_list, key=lambda x: x[1])
    
    # Return the first k elements from the sorted list
    return sorted_tuples[:k]

# Test cases
assert min_k([('Manjeet', 10), ('Akshat', 4), ('Akash', 2), ('Nikhil', 8)], 2) == [('Akash', 2), ('Akshat', 4)]