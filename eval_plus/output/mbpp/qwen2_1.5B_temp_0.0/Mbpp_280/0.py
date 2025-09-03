"""
Write a function that takes in an array and element and returns a tuple containing a boolean that indicates if the element is in the array and the index position of the element (or -1 if the element is not found).
assert sequential_search([11,23,58,31,56,77,43,12,65,19],31) == (True, 3)
"""
def sequential_search(arr, element):
    for i in range(len(arr)):
        if arr[i] == element:
            return True, i
    return False, -1

# Test cases to verify the correctness of the solution
assert sequential_search([11,23,58,31,56,77,43,12,65,19],31) == (True, 3)
assert sequential_search([10,20,30,40,50],60) == (False, -1)
assert sequential_search([],10) == (False, -1)
assert sequential_search([1,2,3,4,5],1) == (True, 0)
assert sequential_search([1,2,3,4,5],6) == (False, -1)