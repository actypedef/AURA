"""
Write a function to find the maximum difference between the number of 0s and number of 1s in any sub-string of the given binary string.
assert find_length("11000010001") == 6
"""
def find_length(binary_string):
    max_diff = 0
    current_diff = 0
    zero_count = 0
    one_count = 0
    
    for char in binary_string:
        if char == '0':
            zero_count += 1
        else:
            one_count += 1
        
        current_diff = zero_count - one_count
        
        if current_diff > max_diff:
            max_diff = current_diff
    
    return max_diff

# Test cases
assert find_length("11000010001") == 6
assert find_length("00110011") == 2
assert find_length("11111111") == 0
assert find_length("00000000") == 0
assert find_length("1010101010101010") == 5