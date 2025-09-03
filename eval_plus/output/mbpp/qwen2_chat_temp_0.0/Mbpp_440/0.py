"""
Write a function to find the first adverb and their positions in a given sentence.
assert find_adverb_position("clearly!! we can see the sky")==(0, 7, 'clearly')
"""
def find_adverb_position(sentence):
    # Split the sentence into words
    words = sentence.split()
    
    # Iterate through each word in the list of words
    for i in range(len(words)):
        # Check if the current word ends with 'ly' which indicates it's an adverb
        if words[i].endswith('ly'):
            # Return the position (index) and the word itself
            return (i, i + len(words[i]), words[i])

# Test the function with the provided test case
assert find_adverb_position("clearly!! we can see the sky") == (0, 7, 'clearly')