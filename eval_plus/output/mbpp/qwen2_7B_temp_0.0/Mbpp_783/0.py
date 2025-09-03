"""
Write a function to convert rgb color to hsv color. https://www.geeksforgeeks.org/program-change-rgb-color-model-hsv-color-model/
assert rgb_to_hsv(255, 255, 255)==(0, 0.0, 100.0)
"""
def rgb_to_hsv(r, g, b):
    # Normalize RGB values to the range [0, 1]
    r /= 255.0
    g /= 255.0
    b /= 255.0
    
    # Find the maximum and minimum of RGB values
    max_color = max(r, g, b)
    min_color = min(r, g, b)
    
    # Calculate the difference between max and min colors
    delta = max_color - min_color
    
    # Determine the hue (H) based on the maximum color
    if delta == 0:
        h = 0
    elif max_color == r:
        h = (60 * ((g - b) / delta)) % 360
    elif max_color == g:
        h = (60 * ((b - r) / delta) + 120) % 360
    else:
        h = (60 * ((r - g) / delta) + 240) % 360
    
    # Calculate the saturation (S)
    s = delta / max_color if max_color != 0 else 0
    
    # Convert the values to percentage
    h *= 1
    s *= 100
    v = max_color * 100
    
    return (h, s, v)

# Test the function with the provided test case
assert rgb_to_hsv(255, 255, 255) == (0, 0.0, 100.0)
