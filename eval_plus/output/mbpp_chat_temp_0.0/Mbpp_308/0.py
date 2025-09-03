"""
Write a function to find the specified number of largest products from two given lists, selecting one factor from each list.
assert large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],3)==[60, 54, 50]
"""
def large_product(list1, list2, N):
    # Calculate all possible products between elements of the two lists
    product = [list1[i] * list2[j] for i in range(len(list1)) for j in range(len(list2))]
    
    # Sort the list of products in descending order
    product.sort(reverse=True)
    
    # Return the first N elements from the sorted list of products
    return product[:N]

# Test the function with the provided test case
assert large_product([1, 2, 3, 4, 5, 6], [3, 6, 8, 9, 10, 6], 3) == [60, 54, 50]