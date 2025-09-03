"""
Write a function to convert more than one list to nested dictionary.
assert convert_list_dictionary(["S001", "S002", "S003", "S004"],["Adina Park", "Leyton Marsh", "Duncan Boyle", "Saim Richards"] ,[85, 98, 89, 92])==[{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}}, {'S004': {'Saim Richards': 92}}]
"""
def convert_list_dictionary(keys, values, scores):
    # Initialize an empty list to store the nested dictionaries
    result = []
    
    # Iterate over the indices of the input lists
    for i in range(len(keys)):
        # Create a nested dictionary with the current key-value-score combination
        nested_dict = {keys[i]: {values[i]: scores[i]}}
        # Append the nested dictionary to the result list
        result.append(nested_dict)
    
    return result

# Test the function with the provided test case
assert convert_list_dictionary(
    ["S001", "S002", "S003", "S004"],
    ["Adina Park", "Leyton Marsh", "Duncan Boyle", "Saim Richards"],
    [85, 98, 89, 92]
) == [
    {'S001': {'Adina Park': 85}},
    {'S002': {'Leyton Marsh': 98}},
    {'S003': {'Duncan Boyle': 89}},
    {'S004': {'Saim Richards': 92}}
]
