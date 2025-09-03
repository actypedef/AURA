"""
Write a function to convert more than one list to nested dictionary.
assert convert_list_dictionary(["S001", "S002", "S003", "S004"],["Adina Park", "Leyton Marsh", "Duncan Boyle", "Saim Richards"] ,[85, 98, 89, 92])==[{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}}, {'S004': {'Saim Richards': 92}}]
"""
def convert_list_dictionary(list1, list2, list3):
    # Use zip to iterate over all three lists simultaneously
    result = [{list1[i]: {list2[i]: list3[i]}} for i in range(len(list1))]
    return result

# Test the function with the provided test case
assert convert_list_dictionary(
    ["S001", "S002", "S003", "S004"],
    ["Adina Park", "Leyton Marsh", "Duncan Boyle", "Saim Richards"],
    [85, 98, 89, 92]
) == [{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}}, {'S004': {'Saim Richards': 92}}]