"""
Write a python function to count the number of pairs whose xor value is odd.
assert find_Odd_Pair([5,4,7,2,1],5) == 6
"""
def find_Odd_Pair(arr, n):
    # Initialize counter for odd XOR pairs
    cnt = 0
    
    # Iterate through each element in the array
    for i in range(n):
        # Compare current element with all other elements
        for j in range(i + 1, n):
            # Check if XOR of the pair is odd
            if (arr[i] ^ arr[j]) % 2 != 0:
                # Increment counter if condition is met
                cnt += 1
                
    return cnt

# Test the function with the provided test case
assert find_Odd_Pair([5, 4, 7, 2, 1], 5) == 6