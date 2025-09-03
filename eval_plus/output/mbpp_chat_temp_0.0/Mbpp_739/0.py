"""
Write a python function to find the index of smallest triangular number with n digits. https://www.geeksforgeeks.org/index-of-smallest-triangular-number-with-n-digits/
assert find_Index(2) == 4
"""
def find_Index(n):
    # Calculate the lower bound for the smallest n-digit number
    low = 10 ** (n - 1)
    
    # Calculate the upper bound for the largest n-digit number
    high = 10 ** n
    
    # Initialize variables for binary search
    start = 1
    end = 10 ** 6
    
    # Perform binary search to find the smallest triangular number with n digits
    while start <= end:
        mid = (start + end) // 2
        
        # Calculate the triangular number at position mid
        tri_num = mid * (mid + 1) // 2
        
        # Check if the calculated triangular number falls within the range
        if tri_num >= low and tri_num <= high:
            return mid
        
        # Adjust the search range based on the comparison
        elif tri_num < low:
            start = mid + 1
        else:
            end = mid - 1

# Test the function with the provided test case
assert find_Index(2) == 4