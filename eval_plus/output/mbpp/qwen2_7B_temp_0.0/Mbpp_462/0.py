"""
Write a function to find all possible combinations of the elements of a given list.
assert combinations_list(['orange', 'red', 'green', 'blue'])==[[], ['orange'], ['red'], ['red', 'orange'], ['green'], ['green', 'orange'], ['green', 'red'], ['green', 'red', 'orange'], ['blue'], ['blue', 'orange'], ['blue', 'red'], ['blue', 'red', 'orange'], ['blue', 'green'], ['blue', 'green', 'orange'], ['blue', 'green', 'red'], ['blue', 'green', 'red', 'orange']]
"""
def combinations_list(nums):
    # Base case: if the list is empty, return a list containing an empty list
    if len(nums) == 0:
        return [[]]
    
    # Recursive case: get combinations for the rest of the list
    rest_combinations = combinations_list(nums[:-1])
    
    # Add each combination from the recursive call to the result
    result = []
    for comb in rest_combinations:
        result.append(comb)
        result.append([nums[-1]] + comb)
    
    return result

# Test the function with the provided test case
assert combinations_list(['orange', 'red', 'green', 'blue']) == [
    [], ['orange'], ['red'], ['red', 'orange'], 
    ['green'], ['green', 'orange'], ['green', 'red'], 
    ['green', 'red', 'orange'], ['blue'], 
    ['blue', 'orange'], ['blue', 'red'], 
    ['blue', 'red', 'orange'], ['blue', 'green'], 
    ['blue', 'green', 'orange'], ['blue', 'green', 'red'], 
    ['blue', 'green', 'red', 'orange']
]