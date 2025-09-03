"""
Write a function to find the specified number of largest products from two given lists, selecting one factor from each list.
assert large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],3)==[60, 54, 50]
"""
def large_product(nums1, nums2, k):
    # Initialize an empty list to store the products
    res = []
    
    # Iterate over each element in the first list
    for i in range(len(nums1)):
        # Iterate over each element in the second list
        for j in range(len(nums2)):
            # Calculate the product of the current elements from both lists
            prod = nums1[i] * nums2[j]
            # Append the product to the result list
            res.append(prod)
    
    # Sort the result list in descending order
    res.sort(reverse=True)
    
    # Return the first 'k' elements from the sorted list
    return res[:k]

# Test the function with the provided test case
assert large_product([1, 2, 3, 4, 5, 6], [3, 6, 8, 9, 10, 6], 3) == [60, 54, 50]
