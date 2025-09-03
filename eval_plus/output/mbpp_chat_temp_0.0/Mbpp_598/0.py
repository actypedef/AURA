"""
Write a function to check whether the given number is armstrong or not.
assert armstrong_number(153)==True
"""
def armstrong_number(n):
    # Convert the number to a string to easily iterate over its digits
    s = str(n)
    # Calculate the length of the number (number of digits)
    l = len(s)
    # Initialize sum to store the sum of each digit raised to the power of the number of digits
    sum = 0
    
    # Iterate over each character in the string representation of the number
    for i in range(l):
        # Convert the character back to an integer and raise it to the power of 'l'
        # Add the result to the sum
        sum += int(s[i]) ** l
    
    # Check if the calculated sum is equal to the original number
    if sum == n:
        return True
    else:
        return False

# Test the function with the provided test case
assert armstrong_number(153) == True