"""
Write a function to extract values between quotation marks " " of the given string.
assert extract_quotation('Cortex "A53" Based "multi" tasking "Processor"') == ['A53', 'multi', 'Processor']
"""
def extract_quotation(s):
    # Split the string into words based on spaces
    words = s.split()
    # Filter out words that contain double quotes
    quoted_words = [word for word in words if '"' in word]
    return quoted_words

# Test cases to verify the correctness of the function
assert extract_quotation('Cortex "A53" Based "multi" tasking "Processor"') == ['A53', 'multi', 'Processor']
assert extract_quotation('"Hello" World "Python"') == ['Hello', 'World', 'Python']
assert extract_quotation('No quotes here') == []