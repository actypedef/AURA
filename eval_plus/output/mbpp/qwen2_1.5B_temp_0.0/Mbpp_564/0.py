"""
Write a python function which takes a list of integers and counts the number of possible unordered pairs where both elements are unequal.
assert count_Pairs([1,2,1],3) == 2
"""
def count_Pairs(arr, n):
    # Initialize counter for pairs
    count = 0
    
    # Iterate through each element in the array
    for i in range(n):
        # Iterate through each element after the current one
        for j in range(i+1, n):
            # Check if the pair consists of unequal elements
            if arr[i] != arr[j]:
                # Increment the counter
                count += 1
                
    return count

# Test the function with provided data points
assert count_Pairs([1,2,1],3) == 2