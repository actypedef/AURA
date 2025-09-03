"""
Write a function that counts the number of pairs of integers in a list that xor to an even number.
assert find_even_pair([5, 4, 7, 2, 1]) == 4
"""
def find_even_pair(arr):
    # Initialize count of pairs
    cnt = 0
    
    # Iterate over each pair of elements in the array
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            # Check if the XOR of the current pair is even
            if (arr[i] ^ arr[j]) % 2 == 0:
                # Increment the count if it is even
                cnt += 1
                
    # Return the total count of pairs with an even XOR value
    return cnt

# Test the function with the provided test case
assert find_even_pair([5, 4, 7, 2, 1]) == 4