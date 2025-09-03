"""
Write a function to find numbers within a given range from startnum ti endnum where every number is divisible by every digit it contains. https://www.w3resource.com/python-exercises/lambda/python-lambda-exercise-24.php
assert divisible_by_digits(1,22)==[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
"""
def divisible_by_digits(startnum, endnum):
    return [i for i in range(startnum, endnum + 1) if all(int(digit) != 0 and i % int(digit) == 0 for digit in str(i))]

# Test cases
assert divisible_by_digits(1,22) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]