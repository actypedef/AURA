"""
Write a function to calculate the wind chill index rounded to the next integer given the wind velocity in km/h and a temperature in celsius.
assert wind_chill(120,35)==40
"""
import math

def wind_chill(v, t):
    # Calculate the wind chill index using the formula
    wci = 13.12 + 0.6215 * t - 11.37 * math.pow(v, 0.16) + 0.3965 * t * math.pow(v, 0.16)
    # Round the result to the nearest integer and return it
    return round(wci)

# Test the function with the provided test case
assert wind_chill(120, 35) == 40
