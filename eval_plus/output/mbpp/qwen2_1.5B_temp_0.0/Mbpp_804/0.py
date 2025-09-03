"""
Write a function to check whether the product of numbers in a list is even or not.
assert is_product_even([1,2,3])
"""
def is_product_even(numbers):
    # Calculate the product of all numbers in the list
    product = 1
    for num in numbers:
        product *= num
    
    # Check if the product is even
    return product % 2 == 0

# Test cases to verify the correctness of the function
assert is_product_even([1,2,3]) == True
assert is_product_even([1,3,5]) == False
assert is_product_even([2,4,6]) == True
assert is_product_even([1,3,7]) == False
assert is_product_even([2,4,8]) == True