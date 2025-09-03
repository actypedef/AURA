"""
Write a python function to find the index of smallest triangular number with n digits. https://www.geeksforgeeks.org/index-of-smallest-triangular-number-with-n-digits/
assert find_Index(2) == 4
"""
def find_Index(n):
    # Calculate the minimum value for n-digit numbers
    min_val = 10 ** (n - 1)
    
    # Calculate the maximum value for n-digit numbers
    max_val = 10 ** n - 1
    
    # Initialize variables to store the result and the current triangular number
    res = 0
    i = 1
    
    # Loop until we find the smallest triangular number greater than or equal to min_val
    while True:
        # Calculate the ith triangular number
        tri_num = i * (i + 1) // 2
        
        # Check if the calculated triangular number is within the range of n-digit numbers
        if min_val <= tri_num <= max_val:
            res = i
            break
        
        # Increment the counter to move to the next triangular number
        i += 1
    
    return res

# Test the function with the provided test case
assert find_Index(2) == 4