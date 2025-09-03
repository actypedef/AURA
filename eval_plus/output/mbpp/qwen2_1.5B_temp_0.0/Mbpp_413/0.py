"""
Write a function to extract the nth element from a given list of tuples.
assert extract_nth_element([('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)] ,0)==['Greyson Fulton', 'Brady Kent', 'Wyatt Knott', 'Beau Turnbull']
"""
def extract_nth_element(tuples_list, n):
    # Extract the nth element from each tuple in the list
    result = [t[n] for t in tuples_list]
    return result

# Test the function with the provided data point
test_data = [('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)]
expected_output = ['Greyson Fulton', 'Brady Kent', 'Wyatt Knott', 'Beau Turnbull']
assert extract_nth_element(test_data, 0) == expected_output