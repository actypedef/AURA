"""
Write a function to check whether the given number is undulating or not.
assert is_undulating(1212121) == True
"""
def is_undulating(num):
    # Convert the number to a string to easily access each digit
    num_str = str(num)
    
    # Check if the length of the number is less than 3
    if len(num_str) < 3:
        return False
    
    # Iterate through the digits of the number
    for i in range(len(num_str) - 2):
        # Check if the current digit is equal to the next two digits
        if num_str[i] == num_str[i + 1] and num_str[i] == num_str[i + 2]:
            return False
    
    # If no three consecutive identical digits are found, it's undulating
    return True

# Test the function with the provided test case
assert is_undulating(1212121) == True