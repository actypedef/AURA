"""
Write a python function to find the sum of the per-digit difference between two integers.
assert digit_distance_nums(1,2) == 1
"""
def digit_distance_nums(num1, num2):
    # Convert both numbers to strings to iterate over each digit
    str_num1 = str(abs(num1))
    str_num2 = str(abs(num2))
    
    # Initialize the result variable to store the sum of differences
    res = 0
    
    # Iterate over each digit in the longer string
    for i in range(max(len(str_num1), len(str_num2))):
        # Get the current digit from each number, defaulting to '0' if out of bounds
        d1 = int(str_num1[i]) if i < len(str_num1) else 0
        d2 = int(str_num2[i]) if i < len(str_num2) else 0
        
        # Add the absolute difference of the digits to the result
        res += abs(d1 - d2)
    
    return res

# Test the function with the provided test case
assert digit_distance_nums(1, 2) == 1