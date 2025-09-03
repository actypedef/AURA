"""
Write a function that counts the number of pairs of integers in a list that xor to an even number.
assert find_even_pair([5, 4, 7, 2, 1]) == 4
"""
def find_even_pair(nums):
    # Initialize a counter for even XOR pairs
    count = 0
    
    # Iterate through each pair of numbers in the list
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            # Check if the XOR of the current pair is even
            if (nums[i] ^ nums[j]) % 2 == 0:
                count += 1
                
    return count

# Test cases to verify the correctness of the solution
assert find_even_pair([5, 4, 7, 2, 1]) == 4
assert find_even_pair([3, 6, 9, 12]) == 6
assert find_even_pair([1, 3, 5, 7]) == 0