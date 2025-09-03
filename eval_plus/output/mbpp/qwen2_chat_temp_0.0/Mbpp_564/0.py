"""
Write a python function which takes a list of integers and counts the number of possible unordered pairs where both elements are unequal.
assert count_Pairs([1,2,1],3) == 2
"""
def count_Pairs(arr, n):
    # Initialize a counter for unequal pairs
    cnt = 0
    
    # Iterate through each element in the array
    for i in range(n):
        # Compare the current element with all subsequent elements
        for j in range(i + 1, n):
            # If the elements are not equal, increment the counter
            if arr[i] != arr[j]:
                cnt += 1
                
    return cnt

# Test the function with the provided test case
assert count_Pairs([1, 2, 1], 3) == 2