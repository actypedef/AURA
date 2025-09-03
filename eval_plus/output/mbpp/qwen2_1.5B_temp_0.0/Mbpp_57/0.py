"""
Write a python function to find the largest number that can be formed with the given list of digits.
assert find_Max_Num([1,2,3]) == 321
"""
def find_Max_Num(digits):
    # Sort the digits in descending order
    digits.sort(reverse=True)
    
    # Convert the sorted digits back into an integer
    max_num = int(''.join(map(str, digits)))
    
    return max_num

# Test cases to verify the correctness of the solution
assert find_Max_Num([1,2,3]) == 321
assert find_Max_Num([4,5,6,7]) == 7654
assert find_Max_Num([8,9,0]) == 980
assert find_Max_Num([0,0,0]) == 0