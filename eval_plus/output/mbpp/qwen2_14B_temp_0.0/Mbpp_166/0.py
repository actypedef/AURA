"""
Write a function that counts the number of pairs of integers in a list that xor to an even number.
assert find_even_pair([5, 4, 7, 2, 1]) == 4
"""
def find_even_pair(arr):
    # Initialize counters for even and odd numbers
    even_count = 0
    odd_count = 0
    
    # Count the number of even and odd numbers in the array
    for num in arr:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    
    # Calculate the number of even XOR pairs
    even_xor_pairs = (even_count * (even_count - 1)) // 2
    # Calculate the number of odd XOR pairs
    odd_xor_pairs = (odd_count * (odd_count - 1)) // 2
    
    # Return the total number of even XOR pairs
    return even_xor_pairs + odd_xor_pairs

# Test the function with the provided test case
assert find_even_pair([5, 4, 7, 2, 1]) == 4
