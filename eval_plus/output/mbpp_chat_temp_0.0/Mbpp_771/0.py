"""
Write a function to check if the given expression is balanced or not. https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-an-expression/
assert check_expression("{()}[{}]") == True
"""
def check_expression(expression):
    # Initialize an empty stack to keep track of opening brackets
    stack = []
    
    # Iterate through each character in the expression
    for char in expression:
        # If the character is an opening bracket, push it onto the stack
        if char in "({[":
            stack.append(char)
        # If the character is a closing bracket
        elif char in ")}]":
            # If the stack is empty, it means there's no matching opening bracket
            if not stack:
                return False
            # Pop the last opening bracket from the stack
            top_element = stack.pop()
            # Check if the popped opening bracket matches the current closing bracket
            if (char == ")" and top_element != "(") or \
               (char == "}" and top_element != "{") or \
               (char == "]" and top_element != "["):
                return False
    
    # If the stack is empty, all brackets were matched; otherwise, they weren't
    return len(stack) == 0

# Test the function with the provided test case
assert check_expression("{()}[{}]") == True