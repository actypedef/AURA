"""
Write a python function which takes a list of integers and counts the number of possible unordered pairs where both elements are unequal.
assert count_Pairs([1,2,1],3) == 2
"""
def count_Pairs(arr, n):
    # Initialize a counter to keep track of unequal pairs
    cnt = 0
    
    # Iterate through each element in the array
    for i in range(n):
        # Compare the current element with all other elements
        for j in range(i + 1, n):
            # Check if the pair (arr[i], arr[j]) is unequal
            if arr[i] != arr[j]:
                # Increment the counter if the pair is unequal
                cnt += 1
                
    # Return the total count of unequal pairs
    return cnt

# Test the function with the provided test case
assert count_Pairs([1, 2, 1], 3) == 2
