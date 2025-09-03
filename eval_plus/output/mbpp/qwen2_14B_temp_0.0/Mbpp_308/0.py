"""
Write a function to find the specified number of largest products from two given lists, selecting one factor from each list.
assert large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],3)==[60, 54, 50]
"""
def large_product(list1, list2, n):
    # Sort both lists in descending order
    list1.sort(reverse=True)
    list2.sort(reverse=True)
    
    # Initialize an empty list to store the largest products
    result = []
    
    # Iterate through the first n elements of each list
    for i in range(n):
        for j in range(n):
            # Calculate the product of elements from both lists
            result.append(list1[i] * list2[j])
    
    # Sort the result list in descending order and return the top n products
    return sorted(result, reverse=True)[:n]

# Test the function with the provided test case
assert large_product([1, 2, 3, 4, 5, 6], [3, 6, 8, 9, 10, 6], 3) == [60, 54, 50]
