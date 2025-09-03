
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
def specialFilter(nums):
    def is_odd_and_greater_than_10(num):
        if num <= 10:
            return False
        str_num = str(abs(num))
        return int(str_num[0]) % 2 == 1 and int(str_num[-1]) % 2 == 1

    count = sum(is_odd_and_greater_than_10(num) for num in nums)
    return count

# Test cases to verify the correctness of the function