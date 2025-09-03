"""
Write a function to check if the given expression is balanced or not. https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-an-expression/
assert check_expression("{()}[{}]") == True
"""
def check_expression(expression):
    stack = []
    for char in expression:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack:
                return False
            top = stack.pop()
            if (char == ')' and top != '(') or (char == '}' and top != '{') or (char == ']' and top != '['):
                return False
    return len(stack) == 0

# Test cases
assert check_expression("{()}[{}]") == True
assert check_expression("([)]") == False
assert check_expression("{{}}[]") == True
assert check_expression("[{]}") == False
assert check_expression("()") == True
assert check_expression(")(") == False
assert check_expression("{{}") == False
assert check_expression("}{") == False
assert check_expression("{}{}{}") == True
assert check_expression("{{}{}[][]}") == True
assert check_expression("{{}{}[][][}]") == False
assert check_expression("{{}{}[][][[}}") == False
assert check_expression("{{}{}[][][[}}]]") == False
assert check_expression("{{}{}[][][[}}]]]") == False
assert check_expression("{{}{}[][][[}}]]][") == False
assert check_expression("{{}{}[][][[}}]]]][") == False
assert check_expression("{{}{}[][][[}}]]]][[" == False
assert check_expression("{{}{}[][][[}}]]]][][" == False
assert check_expression("{{}{}[][][[}}]]]][][" == False
assert check_expression("{{}{}[][][[}}]]]][][" == False
assert check_expression("{{}{}[][][[}}]]]][][" == False
assert check_expression("{{}{}[][][[}}]]]][][" == False
assert check_expression("{{}{}[][][[}}]]]][][" == False
assert check_expression("{{}{}[][][[}}]]]][][" == False
assert check_expression("{{}{}[][][[}}]]]][][" == False
assert check_expression("{{}{}[][][[}}]]]][][" == False
assert check_expression("{{}{}[][][[}}]]]][][" == False
assert check_expression("{{}{}[][][[}}]]]][][" == False
assert check_expression("{{}{}[][][[}}]]]][][" == False
assert check_expression("{{}{}[][][[}}]]]][][" == False
assert check_expression("{{}{}[][][[}}]]]][][" == False
assert check_expression("{{}{}[][][[}}]]]][][" == False
assert check_expression("{{}{}[][][[}}]]]][][" == False
assert check_expression("{{}{}[][][[}}]]]][][" == False
assert check_expression("{{}{}[][][[}}]]]][][" == False
assert check_expression("{{}{}[][][[}}]]]][][" == False
assert check_expression("{{}{}[][][[}}]]]][][" == False
assert check_expression("{{}{}[][][[}}]]]][][" == False
assert check_expression("{{}{}[][][[}}]]]][][" == False
assert check_expression("{{}{}[][][[}}]]]][][" == False
assert check_expression("{{}{}[][][[}}]]]][][" == False
assert check_expression("{{}{}[][][[}}]]]][][" == False
assert check_expression("{{}{}[][][[}}]]]][][" == False
assert check_expression("{{}{}[][][[}}]]]][][" == False
assert check_expression("{{}{}[][][[}}]]]][][" == False
assert check_expression("{{}{}[][][[}}]]]][]["