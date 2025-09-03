"""
Write a function to remove all elements from a given list present in another list.
assert remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8]) == [1, 3, 5, 7, 9, 10]
"""
def remove_elements(main_list, elements_to_remove):
    # Using list comprehension to filter out elements present in elements_to_remove
    filtered_list = [element for element in main_list if element not in elements_to_remove]
    return filtered_list

# Test cases to verify the correctness of the solution
assert remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8]) == [1, 3, 5, 7, 9, 10]
assert remove_elements([10, 20, 30, 40, 50], [10, 30, 50]) == [20, 40]
assert remove_elements([], [1, 2, 3]) == []
assert remove_elements([1, 2, 3], []) == [1, 2, 3]