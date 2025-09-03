"""
Write a function that takes base and power as arguments and calculate the sum of all digits of the base to the specified power.
assert power_base_sum(2,100)==115
"""
def power_base_sum(base, power):
    # Calculate the result of raising 'base' to the power of 'power'
    res = pow(base, power)
    
    # Initialize a variable to store the sum of digits
    sum = 0
    
    # Loop through each digit in the result
    while res > 0:
        # Add the last digit to the sum
        sum += res % 10
        
        # Remove the last digit from the result
        res //= 10
    
    return sum

# Test the function with the provided test case
assert power_base_sum(2, 100) == 115