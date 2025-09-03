"""
Write a python function to find the sum of the per-digit difference between two integers.
assert digit_distance_nums(1,2) == 1
"""
def digit_distance_nums(n1, n2):
    # Convert both numbers to strings to easily access individual digits
    str_n1 = str(n1)
    str_n2 = str(n2)
    
    # Initialize the total sum of differences
    total_sum = 0
    
    # Calculate the length of the longest number
    max_length = max(len(str_n1), len(str_n2))
    
    # Iterate over each digit position
    for i in range(max_length):
        # Get the current digit from each number, filling with '0' if necessary
        digit1 = int(str_n1[i % len(str_n1)]) if i < len(str_n1) else 0
        digit2 = int(str_n2[i % len(str_n2)]) if i < len(str_n2) else 0
        
        # Add the absolute difference of the current digits to the total sum
        total_sum += abs(digit1 - digit2)
    
    return total_sum

# Test the function with the provided test case
assert digit_distance_nums(1, 2) == 1