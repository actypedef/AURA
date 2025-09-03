"""
Write a function to check if the given expression is balanced or not. https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-an-expression/
assert check_expression("{()}[{}]") == True
"""
def check_expression(expression):
    # Initialize an empty stack
    stack = []
    
    # Define a dictionary to hold matching pairs of parentheses
    match_dict = {')': '(', '}': '{', ']': '['}
    
    # Iterate through each character in the expression
    for char in expression:
        # If the character is one of the closing parentheses
        if char in match_dict:
            # Pop from stack and check if it matches the corresponding opening parenthesis
            top_element = stack.pop() if stack else '#'
            
            # If there's no matching opening parenthesis, return False
            if match_dict[char] != top_element:
                return False
        else:
            # Push the opening parenthesis onto the stack
            stack.append(char)
    
    # If the stack is empty, all parentheses were matched; otherwise, return False
    return not stack

# Test the function with the provided test case
assert check_expression("{()}[{}]") == True