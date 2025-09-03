"""
Write a function to convert rgb color to hsv color. https://www.geeksforgeeks.org/program-change-rgb-color-model-hsv-color-model/
assert rgb_to_hsv(255, 255, 255)==(0, 0.0, 100.0)
"""
def rgb_to_hsv(r, g, b):
    # Normalize RGB values to the range [0, 1]
    r /= 255.0
    g /= 255.0
    b /= 255.0
    
    # Find the maximum and minimum of R, G, B
    max_val = max(r, g, b)
    min_val = min(r, g, b)
    
    # Calculate the difference between max and min
    diff = max_val - min_val
    
    # Initialize hue (H), saturation (S), and value (V)
    h, s, v = 0, 0, 0
    
    # Calculate Value (V)
    v = max_val * 100
    
    if diff == 0:
        # If there's no difference, it's grayscale
        h = 0
        s = 0
    else:
        # Calculate Saturation (S)
        s = (diff / max_val) * 100
        
        # Calculate Hue (H)
        if max_val == r:
            h = ((g - b) / diff) % 6
        elif max_val == g:
            h = (b - r) / diff + 2
        else:  # max_val == b
            h = (r - g) / diff + 4
        
        # Convert H from [0, 6] to degrees [0, 360]
        h *= 60
    
    return round(h, 2), round(s, 2), round(v, 2)

# Test the function with the provided test case
assert rgb_to_hsv(255, 255, 255) == (0, 0.0, 100.0)