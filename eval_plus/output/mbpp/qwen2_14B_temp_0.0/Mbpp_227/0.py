"""
Write a function to find minimum of three numbers.
assert min_of_three(10,20,0)==0
"""
def min_of_three(num1, num2, num3):
    # Check if num1 is less than or equal to both num2 and num3
    if (num1 <= num2) and (num1 <= num3):
        smallest = num1
    # Check if num2 is less than or equal to both num1 and num3
    elif (num2 <= num1) and (num2 <= num3):
        smallest = num2
    # If neither of the above conditions is true, num3 is the smallest
    else:
        smallest = num3
    return smallest

# Test the function with the provided test case
assert min_of_three(10, 20, 0) == 0
