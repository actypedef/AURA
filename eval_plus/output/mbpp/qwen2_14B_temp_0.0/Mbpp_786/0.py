"""
Write a function to locate the right insertion point for a specified value in sorted order.
assert right_insertion([1,2,4,5],6)==4
"""
def right_insertion(a, x):
    # Iterate through the list to find the correct insertion point
    for i in range(len(a)):
        if x <= a[i]:
            return i
    # If the value is greater than all elements, return the length of the list
    return len(a)

# Test the function with the provided test case
assert right_insertion([1, 2, 4, 5], 6) == 4
