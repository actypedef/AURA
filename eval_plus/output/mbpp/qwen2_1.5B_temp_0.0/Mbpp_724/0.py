"""
Write a function that takes base and power as arguments and calculate the sum of all digits of the base to the specified power.
assert power_base_sum(2,100)==115
"""
def power_base_sum(base, power):
    # Calculate the result of base raised to the power
    result = base ** power
    
    # Convert the result to a string to iterate over each digit
    str_result = str(result)
    
    # Initialize the sum of digits
    sum_of_digits = 0
    
    # Iterate over each character in the string representation of the result
    for char in str_result:
        # Convert the character back to an integer and add it to the sum
        sum_of_digits += int(char)
    
    return sum_of_digits

# Test cases to verify the correctness of the function
assert power_base_sum(2,100) == 115
assert power_base_sum(3,2) == 9
assert power_base_sum(4,3) == 76