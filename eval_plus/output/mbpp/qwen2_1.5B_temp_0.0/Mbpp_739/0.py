"""
Write a python function to find the index of smallest triangular number with n digits. https://www.geeksforgeeks.org/index-of-smallest-triangular-number-with-n-digits/
assert find_Index(2) == 4
"""
def find_Index(n):
    # The formula for the nth triangular number is n*(n+1)/2
    # To find the smallest triangular number with n digits, we need to find the smallest integer k such that k*(k+1)/2 >= 10^n
    # This can be solved using binary search
    left = 1
    right = 10**n - 1
    
    while left < right:
        mid = (left + right + 1) // 2
        if mid * (mid + 1) // 2 >= 10**n:
            right = mid - 1
        else:
            left = mid
    
    return left

# Test cases
assert find_Index(2) == 4
assert find_Index(3) == 9
assert find_Index(4) == 16
assert find_Index(5) == 25