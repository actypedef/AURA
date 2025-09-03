"""
Write a python function to find a pair with highest product from a given array of integers.
assert max_Product([1,2,3,4,7,0,8,4]) == (7,8)
"""
def max_Product(arr):
    # Initialize variables to store the maximum product found so far and the two numbers that produce it
    max_product = float('-inf')
    num1 = num2 = None
    
    # Iterate through each number in the array
    for num in arr:
        # If the current number is greater than both num1 and num2, update num1 and num2
        if num > max_product:
            num2 = num1
            num1 = num
        # Otherwise, if the current number is greater than num2 but not as large as num1, update num2
        elif num > num2:
            num2 = num
            
    # Return the pair of numbers with the highest product
    return (num1, num2)

# Test the function with the provided test case
assert max_Product([1,2,3,4,7,0,8,4]) == (7,8)