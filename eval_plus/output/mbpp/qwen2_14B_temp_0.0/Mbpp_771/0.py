"""
Write a function to check if the given expression is balanced or not. https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-an-expression/
assert check_expression("{()}[{}]") == True
"""
def check_expression(expression):
    # Dictionary to hold matching pairs of parentheses
    matching_parentheses = {')': '(', '}': '{', ']': '['}
    # Stack to keep track of opening parentheses
    stack = []
    
    # Iterate through each character in the expression
    for char in expression:
        # If the character is an opening parenthesis, push it onto the stack
        if char in matching_parentheses.values():
            stack.append(char)
        # If the character is a closing parenthesis
        elif char in matching_parentheses:
            # Check if the stack is empty or the top of the stack does not match the corresponding opening parenthesis
            if not stack or stack[-1] != matching_parentheses[char]:
                return False
            # Pop the top of the stack
            stack.pop()
    
    # If the stack is empty, all parentheses were matched; otherwise, they were not
    return not stack

# Test the function with the provided test case
assert check_expression("{()}[{}]") == True
