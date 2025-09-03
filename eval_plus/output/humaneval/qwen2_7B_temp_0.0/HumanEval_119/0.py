
def match_parens(lst):
    '''
    You are given a list of two strings, both strings consist of open
    parentheses '(' or close parentheses ')' only.
    Your job is to check if it is possible to concatenate the two strings in
    some order, that the resulting string will be good.
    A string S is considered to be good if and only if all parentheses in S
    are balanced. For example: the string '(())()' is good, while the string
    '())' is not.
    Return 'Yes' if there's a way to make a good string, and return 'No' otherwise.

    Examples:
    match_parens(['()(', ')']) == 'Yes'
    match_parens([')', ')']) == 'No'
    '''
def match_parens(lst):
    '''
    Check if concatenating two strings from the list results in a balanced string.
    
    :param lst: List containing two strings of parentheses
    :return: 'Yes' if a balanced string can be formed, 'No' otherwise
    '''
    # Function to check if a string has balanced parentheses
    def is_balanced(s):
        balance = 0
        for char in s:
            if char == '(':
                balance += 1
            else:
                balance -= 1
            if balance < 0:
                return False
        return balance == 0

    # Try concatenating in both possible orders
    concat1 = lst[0] + lst[1]
    concat2 = lst[1] + lst[0]

    # Check if either concatenated string is balanced
    if is_balanced(concat1) or is_balanced(concat2):
        return 'Yes'
    else:
        return 'No'

# Example usage