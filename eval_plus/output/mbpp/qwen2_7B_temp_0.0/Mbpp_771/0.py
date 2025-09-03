"""
Write a function to check if the given expression is balanced or not. https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-an-expression/
assert check_expression("{()}[{}]") == True
"""
def check_expression(expression):
    # Initialize an empty stack
    stack = []
    
    # Dictionary to hold matching pairs of parentheses
    matches = {')': '(', '}': '{', ']': '['}
    
    # Iterate over each character in the expression
    for char in expression:
        # If the character is an opening bracket, push it onto the stack
        if char in "({[":
            stack.append(char)
        # If the character is a closing bracket
        elif char in ")}]":
            # If the stack is empty or the top of the stack doesn't match the current character, return False
            if not stack or matches[char] != stack.pop():
                return False
    
    # If the stack is empty, all brackets were matched correctly
    return len(stack) == 0

# Test the function with the provided test case
assert check_expression("{()}[{}]") == True
