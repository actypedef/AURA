"""
Write a python function to find the largest number that can be formed with the given list of digits.
assert find_Max_Num([1,2,3]) == 321
"""
def find_Max_Num(digits):
    # Sort the digits in descending order
    digits.sort(reverse=True)
    
    # Initialize an empty string to store the result
    max_num = ""
    
    # Concatenate sorted digits to form the maximum number
    for digit in digits:
        max_num += str(digit)
    
    # Convert the concatenated string back to integer
    return int(max_num)

# Test the function with the provided test case
assert find_Max_Num([1, 2, 3]) == 321
