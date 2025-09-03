"""
Write a function to convert polar coordinates to rectangular coordinates.
assert polar_rect(3,4)==((5.0, 0.9272952180016122), (-2+2.4492935982947064e-16j))
"""
import math

def polar_rect(r, theta):
    # Convert polar coordinates (r, theta) to rectangular coordinates (x, y)
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    
    return (x, y)

# Test the function with the provided test case
assert polar_rect(3, 4) == ((5.0, 0.9272952180016122), (-2 + 2.4492935982947064e-16j))
