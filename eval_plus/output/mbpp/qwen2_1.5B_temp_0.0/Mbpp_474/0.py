"""
Write a function to replace characters in a string.
assert replace_char("polygon",'y','l')==("pollgon")
"""
def replace_char(s, old_char, new_char):
    return s.replace(old_char, new_char)

# Test cases
assert replace_char("polygon",'y','l') == ("pollgon")
assert replace_char("hello world",'o','a') == ("hella world")
assert replace_char("1234567890",'5','x') == ("1234x67890")
assert replace_char("abcdefg",'b','z') == ("acefzg")
assert replace_char("Python Programming","P","p") == ("ython prograaming")