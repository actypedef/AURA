
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
def compare_one(a, b):
    # Convert inputs to floats for comparison, handling comma as decimal separator
    def convert_to_float(value):
        if isinstance(value, str):
            value = value.replace(',', '.')
        return float(value)
    
    # Convert both inputs to floats
    num_a = convert_to_float(a)
    num_b = convert_to_float(b)
    
    # Compare the two numbers
    if num_a > num_b:
        return a
    elif num_b > num_a:
        return b
    else:
        return None

# Test cases