"""
Write a function to extract values between quotation marks " " of the given string.
assert extract_quotation('Cortex "A53" Based "multi" tasking "Processor"') == ['A53', 'multi', 'Processor']
"""
def extract_quotation(s):
    # Split the input string by spaces and filter out words enclosed in double quotes
    return [word.strip('"') for word in s.split() if '"' in word]

# Test the function with the provided test case
assert extract_quotation('Cortex "A53" Based "multi" tasking "Processor"') == ['A53', 'multi', 'Processor']
