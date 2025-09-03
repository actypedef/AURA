"""
Write a function to convert rgb color to hsv color. https://www.geeksforgeeks.org/program-change-rgb-color-model-hsv-color-model/
assert rgb_to_hsv(255, 255, 255)==(0, 0.0, 100.0)
"""
def rgb_to_hsv(r, g, b):
    # Normalize RGB values to be between 0 and 1
    r = r / 255.0
    g = g / 255.0
    b = b / 255.0
    
    # Find the maximum and minimum values of RGB
    max_val = max(r, g, b)
    min_val = min(r, g, b)
    
    # Calculate the difference between max and min values
    diff = max_val - min_val
    
    # Calculate the saturation
    if max_val == 0:
        s = 0
    else:
        s = (diff / max_val) * 100
    
    # Calculate the hue
    if max_val == min_val:
        h = 0
    elif max_val == r:
        h = ((g - b) / diff) % 6
    elif max_val == g:
        h = ((b - r) / diff) + 2
    else:
        h = ((r - g) / diff) + 4
    
    # Convert hue from radians to degrees
    h = h * (180 / 3.14159)
    
    # Return the HSV values as a tuple
    return (h, s, max_val)

# Test the function with the provided test case
assert rgb_to_hsv(255, 255, 255) == (0, 0.0, 100.0)