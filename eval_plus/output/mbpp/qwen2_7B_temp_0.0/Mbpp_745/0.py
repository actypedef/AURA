"""
Write a function to find numbers within a given range from startnum ti endnum where every number is divisible by every digit it contains. https://www.w3resource.com/python-exercises/lambda/python-lambda-exercise-24.php
assert divisible_by_digits(1,22)==[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
"""
def divisible_by_digits(startnum, endnum):
    # Define a lambda function to check if a number is divisible by all its digits
    divisible = lambda x: all(int(digit) != 0 and x % int(digit) == 0 for digit in str(x))
    
    # Use filter to apply the lambda function to the range of numbers
    result = list(filter(divisible, range(startnum, endnum + 1)))
    
    return result

# Test the function with the provided test case
assert divisible_by_digits(1, 22) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]