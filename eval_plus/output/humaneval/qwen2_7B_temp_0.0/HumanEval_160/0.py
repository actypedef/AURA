
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
# Importing necessary packages
import math

def do_algebra(operator, operand):
    """
    This function takes two lists as input: 'operator' containing algebraic operators
    and 'operand' containing integers. It constructs an algebraic expression using these inputs
    and evaluates it.
    
    Parameters:
    operator (list): A list of strings representing algebraic operators ('+', '-', '*', '//', '**').
    operand (list): A list of integers on which the operators will be applied.
    
    Returns:
    int: The evaluated result of the algebraic expression.
    """
    # Initialize the expression with the first operand
    expression = str(operand[0])
    
    # Iterate through the operators and append them along with the next operand to the expression
    for i in range(len(operator)):
        expression += " " + operator[i] + " " + str(operand[i+1])
    
    # Evaluate the expression using eval() and return the result
    return eval(expression)

# Test cases to verify the correctness of the function