
def do_algebra(operator, operand):
    """
    Given two lists operator, and operand. The first list has basic algebra operations, and 
    the second list is a list of integers. Use the two given lists to build the algebric 
    expression and return the evaluation of this expression.

    The basic algebra operations:
    Addition ( + ) 
    Subtraction ( - ) 
    Multiplication ( * ) 
    Floor division ( // ) 
    Exponentiation ( ** ) 

    Example:
    operator['+', '*', '-']
    array = [2, 3, 4, 5]
    result = 2 + 3 * 4 - 5
    => result = 9

    Note:
        The length of operator list is equal to the length of operand list minus one.
        Operand is a list of of non-negative integers.
        Operator list has at least one operator, and operand list has at least two operands.

    """
from typing import List

def do_algebra(operator: List[str], operand: List[int]) -> int:
    # Initialize the result as the first operand
    result = operand[0]

    # Iterate over the operators and operands
    for i, op in enumerate(operator):
        if op == '+':
            result += operand[i+1]
        elif op == '-':
            result -= operand[i+1]
        elif op == '*':
            result *= operand[i+1]
        elif op == '//':
            result //= operand[i+1]
        elif op == '**':
            result **= operand[i+1]

    return result

# Test cases
assert do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9
assert do_algebra(['-', '/', '**'], [10, 2, 3, 2]) == 8
assert do_algebra(['*', '+', '**'], [2, 3, 4, 5]) == 60
assert do_algebra(['**', '-', '+'], [2, 3, 4, 5]) == 17