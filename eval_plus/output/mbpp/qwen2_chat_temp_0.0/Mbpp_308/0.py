"""
Write a function to find the specified number of largest products from two given lists, selecting one factor from each list.
assert large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],3)==[60, 54, 50]
"""
def large_product(nums1, nums2, n):
    # Sort both input lists in ascending order
    nums1.sort()
    nums2.sort()
    
    # Initialize an empty list to store the results
    res = []
    
    # Iterate over the range of n times
    for i in range(n):
        # Calculate the product of the largest elements from both lists
        res.append(nums1[-i - 1] * nums2[-i - 1])
    
    # Return the result as a list
    return res

# Test the function with the provided test case
assert large_product([1, 2, 3, 4, 5, 6], [3, 6, 8, 9, 10, 6], 3) == [60, 54, 50]