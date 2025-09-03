"""
Write a function to check whether the given number is armstrong or not.
assert armstrong_number(153)==True
"""
def armstrong_number(n):
    # Convert the number to string to easily access each digit
    s = str(n)
    total = 0
    
    # Calculate the sum of each digit raised to the power of the number of digits
    for i in range(len(s)):
        total += int(s[i]) ** len(s)
    
    # Check if the calculated sum is equal to the original number
    return total == n

# Test the function with the provided test case
assert armstrong_number(153) == True