"""
Write a function to extract values between quotation marks " " of the given string.
assert extract_quotation('Cortex "A53" Based "multi" tasking "Processor"') == ['A53', 'multi', 'Processor']
"""
import re

def extract_quotation(text):
    # Use regular expression to find all substrings within double quotes
    return re.findall(r'"(.*?)"', text)

# Test the function with the provided test case
assert extract_quotation('Cortex "A53" Based "multi" tasking "Processor"') == ['A53', 'multi', 'Processor']
