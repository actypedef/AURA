"""
Write a function to find numbers within a given range from startnum ti endnum where every number is divisible by every digit it contains. https://www.w3resource.com/python-exercises/lambda/python-lambda-exercise-24.php
assert divisible_by_digits(1,22)==[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
"""
def divisible_by_digits(startnum, endnum):
    # Initialize an empty list to store numbers that meet the criteria
    return_list = []
    
    # Iterate through each number in the specified range
    for num in range(startnum, endnum):
        # Convert the number to a string to check each digit
        s = str(num)
        
        # Check if the number is divisible by each of its digits
        if all(int(digit) != 0 and num % int(digit) == 0 for digit in s):
            return_list.append(num)
    
    return return_list

# Test the function with the provided test case
assert divisible_by_digits(1, 22) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
