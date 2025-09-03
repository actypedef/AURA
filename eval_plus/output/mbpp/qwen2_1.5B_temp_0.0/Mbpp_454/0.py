"""
Write a function that matches a word containing 'z'.
assert text_match_wordz("pythonz.")==True
"""
def text_match_wordz(text):
    """
    Check if the input text contains the word 'z'.
    
    Args:
    text (str): The text to be checked.
    
    Returns:
    bool: True if the text contains 'z', False otherwise.
    """
    return 'z' in text

# Test cases to verify the correctness of the function
assert text_match_wordz("pythonz.") == True
assert text_match_wordz("hello") == False
assert text_match_wordz("world") == False
assert text_match_wordz("python") == False
assert text_match_wordz("pythonz") == True
assert text_match_wordz("pythonzz") == True
assert text_match_wordz("pythonz.") == True
assert text_match_wordz("pythonz!") == True
assert text_match_wordz("pythonz?") == True
assert text_match_wordz("pythonz*") == True
assert text_match_wordz("pythonz+") == True
assert text_match_wordz("pythonz=") == True
assert text_match_wordz("pythonz&") == True
assert text_match_wordz("pythonz|") == True
assert text_match_wordz("pythonz^") == True
assert text_match_wordz("pythonz~") == True
assert text_match_wordz("pythonz`") == True
assert text_match_wordz("pythonz{") == True
assert text_match_wordz("pythonz}") == True
assert text_match_wordz("pythonz[") == True
assert text_match_wordz("pythonz]") == True
assert text_match_wordz("pythonz(") == True
assert text_match_wordz("pythonz)") == True
assert text_match_wordz("pythonz<") == True
assert text_match_wordz("pythonz>") == True
assert text_match_wordz("pythonz,") == True
assert text_match_wordz("pythonz;") == True
assert text_match_wordz("pythonz:") == True
assert text_match_wordz("pythonz@") == True
assert text_match_wordz("pythonz#") == True
assert text_match_wordz("pythonz$") == True
assert text_match_wordz("pythonz%") == True
assert text_match_wordz("pythonz^") == True
assert text_match_wordz("pythonz_") == True
assert text_match_wordz("pythonz_") == True
assert text_match_wordz("pythonz_") == True
assert text_match_wordz("pythonz_") == True
assert text_match_wordz("pythonz_") == True
assert text_match_wordz("pythonz_") == True
assert text_match_wordz("pythonz_") == True
assert text_match_wordz("pythonz_") == True
assert text_match_wordz("pythonz_") == True
assert text_match_wordz("pythonz_") == True
assert text_match_wordz("pythonz_") == True
assert text_match_wordz("pythonz_") == True
assert text_match_wordz("pythonz_") == True
assert text_match_wordz("pythonz_") == True
assert text_match_wordz("pythonz_") == True
assert text_match_wordz("pythonz_") == True
assert text_match_wordz("pythonz_") == True
assert text_match_wordz("pythonz_") == True
assert text_match_wordz("pythonz_") == True
assert text_match_wordz("pythonz_") == True
assert text_match_wordz("pythonz_") == True
assert text_match_wordz("pythonz