"""
Write a function to check whether the given number is armstrong or not.
assert armstrong_number(153)==True
"""
def armstrong_number(n):
    # Convert the number to a string to easily iterate over its digits
    num_str = str(n)
    
    # Calculate the sum of the cubes of each digit
    sum_of_cubes = sum(int(digit) ** 3 for digit in num_str)
    
    # Check if the sum of the cubes equals the original number
    return sum_of_cubes == n

# Test cases to verify the correctness of the function
assert armstrong_number(153) == True
assert armstrong_number(370) == True
assert armstrong_number(9474) == True
assert armstrong_number(9475) == False