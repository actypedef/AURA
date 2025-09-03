"""
Write a python function to count the number of pairs whose xor value is odd.
assert find_Odd_Pair([5,4,7,2,1],5) == 6
"""
def find_Odd_Pair(arr, n):
    # Initialize the count of odd pairs
    count = 0
    
    # Iterate through all possible pairs
    for i in range(n):
        for j in range(i+1, n):
            # Check if the XOR of the pair is odd
            if (arr[i] ^ arr[j]) % 2 != 0:
                count += 1
                
    return count

# Test the function with the provided test case
assert find_Odd_Pair([5,4,7,2,1],5) == 6