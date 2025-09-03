"""
Write a function that takes in a dictionary and integer n and filters the dictionary to only include entries with values greater than or equal to n.
assert dict_filter({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190},170)=={'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}
"""
def dict_filter(dict1, n):
    # Create a new dictionary to store filtered results
    result = {}
    
    # Iterate over each key-value pair in the input dictionary
    for (key, value) in dict1.items():
        # Check if the value is greater than or equal to n
        if value >= n:
            # If condition met, add the key-value pair to the result dictionary
            result[key] = value
    
    return result

# Test the function with the provided test case
assert dict_filter({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}, 170) == {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}