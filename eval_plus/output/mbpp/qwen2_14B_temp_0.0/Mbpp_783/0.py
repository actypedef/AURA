"""
Write a function to convert rgb color to hsv color. https://www.geeksforgeeks.org/program-change-rgb-color-model-hsv-color-model/
assert rgb_to_hsv(255, 255, 255)==(0, 0.0, 100.0)
"""
def rgb_to_hsv(r, g, b):
    # Convert RGB values to the range [0, 1]
    r, g, b = r / 255.0, g / 255.0, b / 255.0
    
    # Find the minimum and maximum values among R, G, B
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx - mn
    
    # Calculate the hue
    if mx == mn:
        h = 0
    elif mx == r:
        h = (60 * ((g - b) / df) + 360) % 360
    elif mx == g:
        h = (60 * ((b - r) / df) + 120) % 360
    elif mx == b:
        h = (60 * ((r - g) / df) + 240) % 360
    
    # Calculate the saturation
    s = 0 if mx == 0 else (df / mx)
    
    # Calculate the value
    v = mx
    
    # Return the HSV values as a tuple
    return (h, s * 100, v * 100)

# Test the function with the provided test case
assert rgb_to_hsv(255, 255, 255) == (0, 0.0, 100.0)
