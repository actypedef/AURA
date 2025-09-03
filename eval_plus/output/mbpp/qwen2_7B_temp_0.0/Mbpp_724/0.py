"""
Write a function that takes base and power as arguments and calculate the sum of all digits of the base to the specified power.
assert power_base_sum(2,100)==115
"""
def power_base_sum(base, power):
    # Calculate the result of raising 'base' to the power of 'power'
    result = pow(base, power)
    
    # Convert the result to a string to iterate over each digit
    result_str = str(result)
    
    # Initialize a variable to store the sum of digits
    sum_of_digits = 0
    
    # Iterate over each character (digit) in the string representation of the result
    for char in result_str:
        # Convert the character back to an integer and add it to the sum
        sum_of_digits += int(char)
    
    return sum_of_digits

# Test the function with the provided test case
assert power_base_sum(2, 100) == 115
