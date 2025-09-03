"""
Write a python function to find the largest number that can be formed with the given list of digits.
assert find_Max_Num([1,2,3]) == 321
"""
def find_Max_Num(digits):
    # Sort the digits in descending order
    digits.sort(reverse=True)
    
    # Initialize an empty string to store the result
    res = ""
    
    # Iterate through each digit and append it to the result string
    for i in range(len(digits)):
        res += str(digits[i])
    
    # Convert the result string back to integer and return
    return int(res)

# Test the function with the provided test case
assert find_Max_Num([1, 2, 3]) == 321
