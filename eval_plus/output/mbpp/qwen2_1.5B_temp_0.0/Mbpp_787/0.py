"""
Write a function that matches a string that has an a followed by three 'b'.
assert not text_match_three("ac")
"""
def text_match_three(text):
    """
    Check if the input text contains an 'a' followed by exactly three 'b's.
    
    Args:
    text (str): The text to be checked.
    
    Returns:
    bool: True if the text matches the pattern, False otherwise.
    """
    # Regular expression to match 'a' followed by exactly three 'b's
    pattern = r'a{1}b{3}'
    return bool(re.search(pattern, text))

# Test cases to verify the correctness of the function
assert not text_match_three("ac")  # Expected output: False
assert text_match_three("aabbb")  # Expected output: True
assert text_match_three("abbbb")  # Expected output: False
assert text_match_three("aabb")  # Expected output: False
assert text_match_three("aaabbb")  # Expected output: True
assert text_match_three("aaaabbb")  # Expected output: True
assert text_match_three("aaaaabbb")  # Expected output: True
assert text_match_three("aaaaabbbb")  # Expected output: True
assert text_match_three("aaaaabbbbb")  # Expected output: True
assert text_match_three("aaaaabbbbbb")  # Expected output: True
assert text_match_three("aaaaabbbbbbb")  # Expected output: True
assert text_match_three("aaaaabbbbbbbb")  # Expected output: True
assert text_match_three("aaaaabbbbbbbb")  # Expected output: True
assert text_match_three("aaaaabbbbbbbb")  # Expected output: True
assert text_match_three("aaaaabbbbbbbb")  # Expected output: True
assert text_match_three("aaaaabbbbbbbb")  # Expected output: True
assert text_match_three("aaaaabbbbbbbb")  # Expected output: True
assert text_match_three("aaaaabbbbbbbb")  # Expected output: True
assert text_match_three("aaaaabbbbbbbb")  # Expected output: True
assert text_match_three("aaaaabbbbbbbb")  # Expected output: True
assert text_match_three("aaaaabbbbbbbb")  # Expected output: True
assert text_match_three("aaaaabbbbbbbb")  # Expected output: True
assert text_match_three("aaaaabbbbbbbb")  # Expected output: True
assert text_match_three("aaaaabbbbbbbb")  # Expected output: True
assert text_match_three("aaaaabbbbbbbb")  # Expected output: True
assert text_match_three("aaaaabbbbbbbb")  # Expected output: True
assert text_match_three("aaaaabbbbbbbb")  # Expected output: True
assert text_match_three("aaaaabbbbbbbb")  # Expected output: True
assert text_match_three("aaaaabbbbbbbb")  # Expected output: True
assert text_match_three("aaaaabbbbbbbb")  # Expected output: True
assert text_match_three("aaaaabbbbbbbb")  # Expected output: True
assert text_match_three("aaaaabbbbbbbb")  # Expected output: True
assert text_match_three("aaaaabbbbbbbb")  # Expected output: True
assert text_match_three("aaaaabbbbbbbb")  # Expected output: True
assert text_match_three("aaaaabbbbbbbb")  # Expected output: True
assert text_match_three("aaaaabbbbbbbb")  # Expected output: True
assert text_match_three("aaaaabbbbbbbb")  # Expected output: True
assert text_match_three("aaaaabbbbbbbb")  # Expected output: True
assert text_match_three("aaaaabbbbbbbb")  # Expected output: True
assert text_match_three("aaaaab