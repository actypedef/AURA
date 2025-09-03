"""
Write a python function to find the volume of a triangular prism.
assert find_Volume(10,8,6) == 240
"""
def find_Volume(base, height, length):
    # Calculate the area of the triangular base using the formula (base * height) / 2
    area = (base * height) / 2
    
    # Calculate the volume of the triangular prism by multiplying the area of the base by the length
    return area * length

# Test the function with the provided test case
assert find_Volume(10, 8, 6) == 240
