"""
Write a function to check whether the given number is armstrong or not.
assert armstrong_number(153)==True
"""
def armstrong_number(n):
    # Convert the number to a string to easily iterate over its digits
    num = str(n)
    
    # Calculate the length of the number (number of digits)
    len_num = len(num)
    
    # Initialize sum variable to store the sum of each digit raised to the power of the number's length
    sum = 0
    
    # Iterate over each digit in the number
    for i in range(len_num):
        # Add the digit raised to the power of the number's length to the sum
        sum += int(num[i]) ** len_num
    
    # Check if the calculated sum equals the original number
    return sum == n

# Test the function with the provided test case
assert armstrong_number(153) == True