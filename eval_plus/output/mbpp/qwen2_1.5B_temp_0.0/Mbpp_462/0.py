"""
Write a function to find all possible combinations of the elements of a given list.
assert combinations_list(['orange', 'red', 'green', 'blue'])==[[], ['orange'], ['red'], ['red', 'orange'], ['green'], ['green', 'orange'], ['green', 'red'], ['green', 'red', 'orange'], ['blue'], ['blue', 'orange'], ['blue', 'red'], ['blue', 'red', 'orange'], ['blue', 'green'], ['blue', 'green', 'orange'], ['blue', 'green', 'red'], ['blue', 'green', 'red', 'orange']]
"""
def combinations_list(lst):
    # Initialize an empty list to store all combinations
    result = [[]]
    
    # Iterate over each element in the input list
    for item in lst:
        # Create a new list to hold the current combination
        temp_result = []
        
        # Iterate over each existing combination in the result list
        for comb in result:
            # Add the current item to each existing combination
            temp_result.append(comb + [item])
        
        # Update the result list with the new combinations
        result.extend(temp_result)
    
    return result

# Test the function with the provided data point
assert combinations_list(['orange', 'red', 'green', 'blue']) == [
    [],
    ['orange'],
    ['red'],
    ['red', 'orange'],
    ['green'],
    ['green', 'orange'],
    ['green', 'red'],
    ['green', 'red', 'orange'],
    ['blue'],
    ['blue', 'orange'],
    ['blue', 'red'],
    ['blue', 'red', 'orange'],
    ['blue', 'green'],
    ['blue', 'green', 'orange'],
    ['blue', 'green', 'red'],
    ['blue', 'green', 'red', 'orange']
]