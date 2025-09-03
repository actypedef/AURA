"""
Write a python function to find the largest number that can be formed with the given list of digits.
assert find_Max_Num([1,2,3]) == 321
"""
def find_Max_Num(digits):
    # Convert the list of digits to a string
    digits_str = ''.join(map(str, digits))
    
    # Sort the string in descending order
    sorted_digits_str = ''.join(sorted(digits_str, reverse=True))
    
    # Convert the sorted string back to an integer
    max_num = int(sorted_digits_str)
    
    return max_num

# Test the function
assert find_Max_Num([1,2,3]) == 321
assert find_Max_Num([4,5,6,7]) == 7654
assert find_Max_Num([0,0,0,1]) == 1000