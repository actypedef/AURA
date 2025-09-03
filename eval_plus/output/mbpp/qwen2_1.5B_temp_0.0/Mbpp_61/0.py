"""
Write a python function to count the number of substrings with the sum of digits equal to their length.
assert count_Substrings('112112') == 6
"""
def count_substrings(s):
    # Initialize variables
    count = 0
    current_sum = 0
    
    # Dictionary to store the frequency of cumulative sums
    sum_freq = {0: 1}
    
    for char in s:
        # Update the current sum
        current_sum += int(char)
        
        # Calculate the difference between current sum and target (length of substring)
        diff = current_sum - len(s)
        
        # If this difference exists in the dictionary, add its frequency to the count
        if diff in sum_freq:
            count += sum_freq[diff]
        
        # Update the dictionary with the current sum's frequency
        if current_sum not in sum_freq:
            sum_freq[current_sum] = 0
        sum_freq[current_sum] += 1
    
    return count

# Test cases
assert count_substrings('112212') == 6
assert count_substrings('123456789') == 36
assert count_substrings('11111111') == 15
assert count_substrings('0') == 1
assert count_substrings('9') == 1
assert count_substrings('10') == 1
assert count_substrings('11') == 1
assert count_substrings('12') == 1
assert count_substrings('13') == 1
assert count_substrings('14') == 1
assert count_substrings('15') == 1
assert count_substrings('16') == 1
assert count_substrings('17') == 1
assert count_substrings('18') == 1
assert count_substrings('19') == 1
assert count_substrings('20') == 1
assert count_substrings('21') == 1
assert count_substrings('22') == 1
assert count_substrings('23') == 1
assert count_substrings('24') == 1
assert count_substrings('25') == 1
assert count_substrings('26') == 1
assert count_substrings('27') == 1
assert count_substrings('28') == 1
assert count_substrings('29') == 1
assert count_substrings('30') == 1
assert count_substrings('31') == 1
assert count_substrings('32') == 1
assert count_substrings('33') == 1
assert count_substrings('34') == 1
assert count_substrings('35') == 1
assert count_substrings('36') == 1
assert count_substrings('37') == 1
assert count_substrings('38') == 1
assert count_substrings('39') == 1
assert count_substrings('40') == 1
assert count_substrings('41') == 1
assert count_substrings('42') == 1
assert count_substrings('43') == 1
assert count_substrings('44') == 1
assert count_substrings('45') == 1
assert count_substrings('46') == 1
assert count_substrings('47') == 1
assert count_substrings('48') == 1
assert count_substrings('49') == 1
assert count_substrings('50') == 1
assert count_substrings('51') == 1
assert count_substrings('52') == 1
assert