"""
Write a function to convert polar coordinates to rectangular coordinates.
assert polar_rect(3,4)==((5.0, 0.9272952180016122), (-2+2.4492935982947064e-16j))
"""
import cmath

def polar_rect(r, theta):
    # Convert polar coordinates (r, theta) to rectangular coordinates using cmath.rect()
    rect_coordinates = cmath.rect(r, theta)
    
    # Extract real and imaginary parts of the complex number
    x = rect_coordinates.real
    y = rect_coordinates.imag
    
    return ((x, y))

# Test the function with the provided test case
assert polar_rect(3, 4) == ((5.0, 0.9272952180016122), (-2 + 2.4492935982947064e-16j))