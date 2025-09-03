"""
Write a function to extract values between quotation marks " " of the given string.
assert extract_quotation('Cortex "A53" Based "multi" tasking "Processor"') == ['A53', 'multi', 'Processor']
"""
def extract_quotation(string):
    # Splitting the input string by spaces and extracting words within quotation marks
    return [word.strip('"') for word in string.split(" ") if '"' in word]

# Test case to verify the correctness of the function
assert extract_quotation('Cortex "A53" Based "multi" tasking "Processor"') == ['A53', 'multi', 'Processor']
