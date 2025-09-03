"""
Write a python function to find the product of the array multiplication modulo n.
assert find_remainder([ 100, 10, 5, 25, 35, 14 ],11) ==9
"""
def find_remainder(arr, n):
    # Initialize the result variable to 1 (since multiplying any number by 1 doesn't change it)
    result = 1
    
    # Iterate through each element in the array
    for num in arr:
        # Multiply the current result by the current number and take modulo n
        result = (result * num) % n
    
    return result

# Test the function with the provided test case
assert find_remainder([ 100, 10, 5, 25, 35, 14 ],11) == 9