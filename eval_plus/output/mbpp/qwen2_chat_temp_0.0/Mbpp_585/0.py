"""
Write a function to find the n most expensive items in a given dataset.
assert expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}],1)==[{'name': 'Item-2', 'price': 555.22}]
"""
def expensive_items(items, n):
    # Sort the list of items based on their price in descending order
    sorted_items = sorted(items, key=lambda x: x['price'], reverse=True)
    
    # Return the first n items from the sorted list
    return sorted_items[:n]

# Test the function with the provided test case
assert expensive_items([{'name': 'Item-1', 'price': 101.1}, {'name': 'Item-2', 'price': 555.22}], 1) == [{'name': 'Item-2', 'price': 555.22}]