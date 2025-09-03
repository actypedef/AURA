"""
Write a function to convert rgb color to hsv color. https://www.geeksforgeeks.org/program-change-rgb-color-model-hsv-color-model/
assert rgb_to_hsv(255, 255, 255)==(0, 0.0, 100.0)
"""
def rgb_to_hsv(r, g, b):
    # Normalize RGB values to the range [0, 1]
    r /= 255.0
    g /= 255.0
    b /= 255.0
    
    # Calculate maximum and minimum of RGB values
    max_val = max(r, g, b)
    min_val = min(r, g, b)
    
    # Calculate the difference between max and min
    delta = max_val - min_val
    
    # Calculate hue (H)
    if delta == 0:
        h = 0
    elif max_val == r:
        h = ((g - b) / delta) % 6
    elif max_val == g:
        h = ((b - r) / delta + 2) % 6
    else:  # max_val == b
        h = ((r - g) / delta + 4) % 6
    
    # Convert hue from radians to degrees
    h *= 60
    
    # Calculate saturation (S)
    if max_val == 0:
        s = 0
    else:
        s = (delta / max_val) * 100
    
    # Calculate value (V)
    v = max_val * 100
    
    return (h, s, v)

# Test the function with the provided test case
assert rgb_to_hsv(255, 255, 255) == (0, 0.0, 100.0)