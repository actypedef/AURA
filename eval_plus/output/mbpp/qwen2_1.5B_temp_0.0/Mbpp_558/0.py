"""
Write a python function to find the sum of the per-digit difference between two integers.
assert digit_distance_nums(1,2) == 1
"""
def digit_distance_nums(num1, num2):
    # Convert numbers to strings to easily iterate over each digit
    str_num1 = str(num1)
    str_num2 = str(num2)
    
    # Initialize the sum of differences
    total_diff = 0
    
    # Iterate over each digit in both numbers
    for i in range(len(str_num1)):
        # Calculate the absolute difference between the digits at the same position
        diff = abs(int(str_num1[i]) - int(str_num2[i]))
        
        # Add the difference to the total sum
        total_diff += diff
    
    return total_diff

# Test cases to verify the correctness of the function
assert digit_distance_nums(1,2) == 1
assert digit_distance_nums(15, 47) == 8
assert digit_distance_nums(99, 11) == 8
assert digit_distance_nums(123, 456) == 12