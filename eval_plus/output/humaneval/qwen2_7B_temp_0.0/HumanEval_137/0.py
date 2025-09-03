
def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,

    compare_one(1, 2.5) ➞ 2.5
    compare_one(1, "2,3") ➞ "2,3"
    compare_one("5,1", "6") ➞ "6"
    compare_one("1", 1) ➞ None
    """
import re

def compare_one(a, b):
    # Convert both inputs to strings for uniform comparison
    str_a = str(a)
    str_b = str(b)

    # Remove commas from string representations of numbers
    str_a = re.sub(r',', '.', str_a)
    str_b = re.sub(r',', '.', str_b)

    # Try converting strings to float, handle exceptions if conversion fails
    try:
        float_a = float(str_a)
        float_b = float(str_b)
    except ValueError:
        return None

    # Compare the float values
    if float_a > float_b:
        return a
    elif float_b > float_a:
        return b
    else:
        return None

# Test cases