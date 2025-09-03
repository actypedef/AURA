"""
Write a python function to find the index of smallest triangular number with n digits. https://www.geeksforgeeks.org/index-of-smallest-triangular-number-with-n-digits/
assert find_Index(2) == 4
"""
def find_Index(n):
    # Calculate the lower bound for n-digit numbers
    lb = 10 ** (n - 1)
    
    # Calculate the upper bound for n-digit numbers
    ub = 10 ** n
    
    # Initialize variables to store the result and count
    res = 0
    count = 0
    
    # Iterate through the range to find the smallest triangular number
    while True:
        # Increment count for each iteration
        count += 1
        
        # Calculate the triangular number using the formula
        tri_num = int(count * (count + 1) / 2)
        
        # Check if the calculated triangular number falls within the bounds
        if tri_num >= lb and tri_num <= ub:
            res = count
            break

    return res

# Test the function with the provided test case
assert find_Index(2) == 4
