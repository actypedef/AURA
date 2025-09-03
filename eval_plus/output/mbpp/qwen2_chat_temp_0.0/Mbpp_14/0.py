"""
Write a python function to find the volume of a triangular prism.
assert find_Volume(10,8,6) == 240
"""
def find_Volume(base, height, length):
    # Calculate the area of the base triangle using the formula: (base * height) / 2
    base_area = (base * height) / 2
    
    # Calculate the volume of the triangular prism using the formula: base_area * length
    volume = base_area * length
    
    return volume

# Test the function with the provided test case
assert find_Volume(10, 8, 6) == 240
