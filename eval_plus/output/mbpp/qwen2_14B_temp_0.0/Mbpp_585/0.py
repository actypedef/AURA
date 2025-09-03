"""
Write a function to find the n most expensive items in a given dataset.
assert expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}],1)==[{'name': 'Item-2', 'price': 555.22}]
"""
import heapq

def expensive_items(items, n):
    # Use heapq.nlargest to find the n items with the highest prices
    expensive_items = heapq.nlargest(n, items, key=lambda s: s['price'])
    return expensive_items

# Test the function with the provided test case
assert expensive_items([{'name': 'Item-1', 'price': 101.1}, {'name': 'Item-2', 'price': 555.22}], 1) == [{'name': 'Item-2', 'price': 555.22}]
