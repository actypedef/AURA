"""
Write a function to extract values between quotation marks " " of the given string.
assert extract_quotation('Cortex "A53" Based "multi" tasking "Processor"') == ['A53', 'multi', 'Processor']
"""
def extract_quotation(s):
    # Split the string by spaces and filter out elements that contain double quotes
    return [i for i in s.split() if '"' in i]

# Test the function with the provided test case
assert extract_quotation('Cortex "A53" Based "multi" tasking "Processor"') == ['A53', 'multi', 'Processor']
