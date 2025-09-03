"""
Write a function to find all possible combinations of the elements of a given list.
assert combinations_list(['orange', 'red', 'green', 'blue'])==[[], ['orange'], ['red'], ['red', 'orange'], ['green'], ['green', 'orange'], ['green', 'red'], ['green', 'red', 'orange'], ['blue'], ['blue', 'orange'], ['blue', 'red'], ['blue', 'red', 'orange'], ['blue', 'green'], ['blue', 'green', 'orange'], ['blue', 'green', 'red'], ['blue', 'green', 'red', 'orange']]
"""
def combinations_list(nums):
    # Base case: if the list is empty, return a list containing an empty list
    if len(nums) == 0:
        return [[]]
    
    # Recursive case: get combinations without the first element
    combs_without_first = combinations_list(nums[1:])
    
    # Add the first element to each combination obtained from the recursive call
    combs_with_first = [[nums[0]] + comb for comb in combs_without_first]
    
    # Combine both sets of combinations
    return combs_without_first + combs_with_first

# Test the function with the provided test case
assert combinations_list(['orange', 'red', 'green', 'blue']) == [
    [], ['orange'], ['red'], ['red', 'orange'], ['green'], ['green', 'orange'], 
    ['green', 'red'], ['green', 'red', 'orange'], ['blue'], ['blue', 'orange'], 
    ['blue', 'red'], ['blue', 'red', 'orange'], ['blue', 'green'], ['blue', 'green', 'orange'], 
    ['blue', 'green', 'red'], ['blue', 'green', 'red', 'orange']
]