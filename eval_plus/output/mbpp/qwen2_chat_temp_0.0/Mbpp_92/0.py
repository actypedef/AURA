"""
Write a function to check whether the given number is undulating or not.
assert is_undulating(1212121) == True
"""
def is_undulating(num):
    # Convert the number to a string to easily access individual digits
    num_str = str(num)
    
    # Check if the length of the number is less than 3 or if it's even
    if len(num_str) < 3 or len(num_str) % 2 == 0:
        return False
    
    # Extract the first two digits
    first_two_digits = int(num_str[:2])
    
    # Iterate through the number in steps of 2
    for i in range(2, len(num_str), 2):
        # If any pair of consecutive digits does not match the first two digits, return False
        if int(num_str[i:i+2]) != first_two_digits:
            return False
    
    # If all pairs match, return True
    return True

# Test the function with the provided test case
assert is_undulating(1212121) == True