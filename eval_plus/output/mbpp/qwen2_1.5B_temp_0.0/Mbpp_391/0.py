"""
Write a function to convert more than one list to nested dictionary.
assert convert_list_dictionary(["S001", "S002", "S003", "S004"],["Adina Park", "Leyton Marsh", "Duncan Boyle", "Saim Richards"] ,[85, 98, 89, 92])==[{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}}, {'S004': {'Saim Richards': 92}}]
"""
def convert_list_dictionary(list_keys, list_values):
    # Create an empty dictionary
    result = {}
    
    # Iterate over the keys and values simultaneously
    for key, value in zip(list_keys, list_values):
        # If the key already exists in the dictionary, add the value as a new item under it
        if key in result:
            result[key].update({value: None})
        else:
            # Otherwise, create a new dictionary for the key and add the value as its first item
            result[key] = {value: None}
    
    return result

# Test the function with the provided data points
assert convert_list_dictionary(["S001", "S002", "S003", "S004"], ["Adina Park", "Leyton Marsh", "Duncan Boyle", "Saim Richards"], [85, 98, 89, 92]) == [{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}}, {'S004': {'Saim Richards': 92}}]