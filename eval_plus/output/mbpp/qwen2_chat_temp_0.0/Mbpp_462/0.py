"""
Write a function to find all possible combinations of the elements of a given list.
assert combinations_list(['orange', 'red', 'green', 'blue'])==[[], ['orange'], ['red'], ['red', 'orange'], ['green'], ['green', 'orange'], ['green', 'red'], ['green', 'red', 'orange'], ['blue'], ['blue', 'orange'], ['blue', 'red'], ['blue', 'red', 'orange'], ['blue', 'green'], ['blue', 'green', 'orange'], ['blue', 'green', 'red'], ['blue', 'green', 'red', 'orange']]
"""
def combinations_list(colors):
    # Initialize an empty list to store all combinations
    result = []
    
    # Iterate over each color in the input list
    for i in range(len(colors)):
        # For each color, iterate over the current result list
        for j in range(len(result)):
            # Append the current combination with the new color
            result.append(result[j] + [colors[i]])
        # Add the single-color combination to the result list
        result.append([colors[i]])
    
    return result

# Test the function with the provided test case
assert combinations_list(['orange', 'red', 'green', 'blue']) == [
    [], ['orange'], ['red'], ['red', 'orange'], ['green'],
    ['green', 'orange'], ['green', 'red'], ['green', 'red', 'orange'],
    ['blue'], ['blue', 'orange'], ['blue', 'red'], ['blue', 'red', 'orange'],
    ['blue', 'green'], ['blue', 'green', 'orange'], ['blue', 'green', 'red'],
    ['blue', 'green', 'red', 'orange']
]