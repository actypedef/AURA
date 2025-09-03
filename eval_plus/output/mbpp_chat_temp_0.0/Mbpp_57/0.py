"""
Write a python function to find the largest number that can be formed with the given list of digits.
assert find_Max_Num([1,2,3]) == 321
"""
def find_Max_Num(digits):
    # Sort the digits in descending order
    digits.sort(reverse=True)
    
    # Initialize an empty string to store the result
    max_num = ""
    
    # Iterate through the sorted digits and append them to the result string
    for i in range(len(digits)):
        max_num += str(digits[i])
    
    # Convert the result string back to an integer and return it
    return int(max_num)

# Test the function with the provided test case
assert find_Max_Num([1, 2, 3]) == 321