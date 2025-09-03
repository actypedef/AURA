"""
Write a function which takes a tuple of tuples and returns the average value for each tuple as a list.
assert average_tuple(((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4)))==[30.5, 34.25, 27.0, 23.25]
"""
def average_tuple(test_list):
    # Calculate the average of each sub-tuple and store it in a list
    res = [sum(sub) / len(sub) for sub in test_list]
    return res

# Test the function with the provided test case
assert average_tuple(((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))) == [30.5, 34.25, 27.0, 23.25]
