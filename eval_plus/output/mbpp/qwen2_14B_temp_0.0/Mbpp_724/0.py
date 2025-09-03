"""
Write a function that takes base and power as arguments and calculate the sum of all digits of the base to the specified power.
assert power_base_sum(2,100)==115
"""
def power_base_sum(base, power):
    # Calculate the result of raising base to the specified power
    result = base ** power
    
    # Convert the result to a string and sum its digits
    return sum(int(digit) for digit in str(result))

# Test the function with the provided test case
assert power_base_sum(2, 100) == 115
