"""
Write a python function to check if the elements of a given list are unique or not.
assert all_unique([1,2,3]) == True
"""
def all_unique(data):
    # Create an empty set to store unique elements
    seen = set()
    
    # Iterate over each element in the data list
    for x in data:
        # Check if the element is already in the set
        if x in seen:
            return False  # If found, return False indicating duplicates exist
        else:
            seen.add(x)  # Add the element to the set
    
    return True  # If no duplicates were found, return True

# Test the function with the provided test case
assert all_unique([1, 2, 3]) == True