"""
Write a python function to count the number of pairs whose xor value is odd.
assert find_Odd_Pair([5,4,7,2,1],5) == 6
"""
def find_Odd_Pair(arr, n):
    odd_count = 0
    even_count = 0
    
    # Count the number of odd and even elements in the array
    for i in range(0, n):
        if arr[i] & 1:
            odd_count += 1
        else:
            even_count += 1
    
    # Calculate the number of odd pairs
    odd_pair_count = odd_count * even_count
    
    return odd_pair_count

# Test the function with the provided test case
assert find_Odd_Pair([5, 4, 7, 2, 1], 5) == 6
