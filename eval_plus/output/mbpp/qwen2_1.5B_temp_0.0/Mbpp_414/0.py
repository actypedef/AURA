"""
Write a python function to check whether any value in a sequence exists in a sequence or not.
assert overlapping([1,2,3,4,5],[6,7,8,9]) == False
"""
def overlapping(seq1, seq2):
    return any(item in seq2 for item in seq1)

# Test cases
assert overlapping([1,2,3,4,5], [6,7,8,9]) == False
assert overlapping([10, 20, 30], [40, 50, 60]) == True
assert overlapping(['apple', 'banana'], ['cherry', 'date']) == False
assert overlapping(['hello', 'world'], ['hello', 'python']) == True