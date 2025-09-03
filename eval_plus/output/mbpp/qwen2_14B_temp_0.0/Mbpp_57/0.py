"""
Write a python function to find the largest number that can be formed with the given list of digits.
assert find_Max_Num([1,2,3]) == 321
"""
def find_Max_Num(nums):
    # Convert each digit to a string and sort the list in descending order
    nums = sorted(nums, reverse=True)
    
    # Concatenate the sorted digits into a single number
    max_num = int("".join(map(str, nums)))
    
    return max_num

# Test the function with the provided test case
assert find_Max_Num([1, 2, 3]) == 321
