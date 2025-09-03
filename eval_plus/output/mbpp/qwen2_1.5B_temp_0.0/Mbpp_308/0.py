"""
Write a function to find the specified number of largest products from two given lists, selecting one factor from each list.
assert large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],3)==[60, 54, 50]
"""
def large_product(list1, list2, n):
    # Sort both lists in descending order
    list1.sort(reverse=True)
    list2.sort(reverse=True)
    
    # Initialize an empty list to store the results
    result = []
    
    # Iterate over the first 'n' elements of list1
    for i in range(n):
        # Multiply the current element of list1 with the first 'n' elements of list2
        product = list1[i] * list2[:n]
        # Append the product to the result list
        result.append(product)
    
    return result

# Test the function with the provided data points
assert large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],3)==[60, 54, 50]