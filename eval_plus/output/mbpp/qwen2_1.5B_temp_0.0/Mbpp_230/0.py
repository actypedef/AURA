"""
Write a function that takes in a string and character, replaces blank spaces in the string with the character, and returns the string.
assert replace_blank("hello people",'@')==("hello@people")
"""
def replace_blank(s, c):
    return s.replace(' ', c)

# Test cases to verify the correctness of the solution
assert replace_blank("hello people",'@')==("hello@people")
assert replace_blank("Python programming","-")==("Python-programming")
assert replace_blank("1234567890","*")==("*"*10)
assert replace_blank("No blanks here!","_")==("No_blanks_here!")