"""
Write a python function to find the sum of non-repeated elements in a given list.
assert find_sum([1,2,3,1,1,4,5,6]) == 21
"""
def find_sum(nums):
    # Initialize the sum to zero
    total = 0
    
    # Iterate through each number in the list
    for num in nums:
        # Check if the count of the number in the list is exactly one
        if nums.count(num) == 1:
            # Add the number to the total sum
            total += num
            
    # Return the total sum of non-repeated elements
    return total

# Test the function with the provided test case
assert find_sum([1, 2, 3, 1, 1, 4, 5, 6]) == 21