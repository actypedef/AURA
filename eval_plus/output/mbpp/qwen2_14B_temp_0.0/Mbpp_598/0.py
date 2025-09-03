"""
Write a function to check whether the given number is armstrong or not.
assert armstrong_number(153)==True
"""
def armstrong_number(num):
    # Initialize sum to 0
    sum = 0
    
    # Temporarily store the original number
    temp = num
    
    # Calculate the number of digits in the number
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    
    # Check if the sum of cubes of digits is equal to the original number
    if num == sum:
        return True
    else:
        return False

# Test the function with the provided test case
assert armstrong_number(153) == True
