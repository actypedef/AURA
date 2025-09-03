"""
Write a function to find the maximum product formed by multiplying numbers of an increasing subsequence of that array.
assert max_product([3, 100, 4, 5, 150, 6]) == 3000
"""
def max_product(arr):
    n = len(arr)
    
    # Initialize the list to store the maximum product subsequence ending at each index
    mp = [0] * n
    
    # The maximum product subsequence ending at the first element is the element itself
    mp[0] = arr[0]
    
    # Iterate through the array starting from the second element
    for i in range(1, n):
        # Initialize the current maximum product as the element itself
        curr_max = arr[i]
        
        # Check all previous elements to find the maximum product subsequence
        for j in range(i):
            if arr[j] < arr[i]:
                curr_max = max(curr_max, mp[j] * arr[i])
        
        # Update the maximum product subsequence ending at the current index
        mp[i] = curr_max
    
    # Return the maximum value from the mp list
    return max(mp)

# Test the function with the provided test case
assert max_product([3, 100, 4, 5, 150, 6]) == 3000