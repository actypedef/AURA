"""
Write a function to find the occurrence and position of the substrings within a string. Return None if there is no match.
assert occurance_substring('python programming, python language','python')==('python', 0, 6)
"""
def occurance_substring(string, substring):
    # Find all occurrences of the substring in the string
    matches = [match.start() for match in re.finditer(substring, string)]
    
    # If no matches found, return None
    if not matches:
        return None
    
    # Return the first match's start index, end index, and the substring itself
    return (substring, matches[0], matches[-1])

# Test cases
assert occurance_substring('python programming, python language','python') == ('python', 0, 6)
assert occurance_substring('hello world', 'world') == ('world', 7, 12)
assert occurance_substring('data science', 'science') == ('science', 8, 14)
assert occurance_substring('machine learning', 'learning') == ('learning', 9, 15)
assert occurance_substring(' artificial intelligence', 'intelligence') == ('intelligence', 13, 20)
assert occurance_substring('deep learning', 'learning') == ('learning', 10, 16)
assert occurance_substring('natural language processing', 'processing') == ('processing', 16, 24)
assert occurance_substring('computer vision', 'vision') == ('vision', 11, 17)
assert occurance_substring(' robotics', 'robotics') == ('robotics', 0, 8)
assert occurance_substring('artificial intelligence', 'AI') == ('AI', 0, 2)
assert occurance_substring('machine learning', 'ML') == ('ML', 8, 10)
assert occurance_substring('deep learning', 'DL') == ('DL', 10, 12)
assert occurance_substring('natural language processing', 'NLP') == ('NLP', 16, 18)
assert occurance_substring('computer vision', 'CV') == ('CV', 11, 13)
assert occurance_substring(' robotics', 'ROBOTICS') == ('ROBOTICS', 0, 10)
assert occurance_substring('artificial intelligence', 'AI') == ('AI', 0, 2)
assert occurance_substring('machine learning', 'ML') == ('ML', 8, 10)
assert occurance_substring('deep learning', 'DL') == ('DL', 10, 12)
assert occurance_substring('natural language processing', 'NLP') == ('NLP', 16, 18)
assert occurance_substring('computer vision', 'CV') == ('CV', 11, 13)
assert occurance_substring(' robotics', 'ROBOTICS') == ('ROBOTICS', 0, 10)
assert occurance_substring('artificial intelligence', 'AI') == ('AI', 0, 2)
assert occurance_substring('machine learning', 'ML') == ('ML', 8, 10)
assert occurance_substring('deep learning', 'DL') == ('DL', 10, 12)
assert occurance_substring('natural language processing', 'NLP') == ('NLP', 16, 18)
assert occurance_substring('computer vision', 'CV') == ('CV', 11, 13)
assert occurance_substring(' robotics', 'ROBOTICS') == ('ROBOTICS', 0, 10)
assert occurance_substring('artificial intelligence', 'AI') == ('AI', 0,