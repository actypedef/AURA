"""
Write a function to flatten a list and sum all of its elements.
assert recursive_list_sum(([1, 2, [3,4],[5,6]]))==21
"""
def recursive_list_sum(data_list):
    total = 0
    for element in data_list:
        if isinstance(element, list):
            total += recursive_list_sum(element)
        else:
            total += element
    return total

# Test the function with the provided test case
assert recursive_list_sum([1, 2, [3, 4], [5, 6]]) == 21