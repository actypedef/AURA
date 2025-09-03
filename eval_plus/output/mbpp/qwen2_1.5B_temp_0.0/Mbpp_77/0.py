"""
Write a python function to find whether a number is divisible by 11.
assert is_Diff (12345) == False
"""
def is_Diff(n):
    # Convert the number to string to easily access each digit
    str_n = str(n)
    
    # Calculate the sum of digits at even positions
    sum_even = sum(int(str_n[i]) for i in range(0, len(str_n), 2))
    
    # Calculate the sum of digits at odd positions
    sum_odd = sum(int(str_n[i]) for i in range(1, len(str_n), 2))
    
    # Check if the difference between the two sums is divisible by 11
    return abs(sum_even - sum_odd) % 11 == 0

# Test cases
assert is_Diff(12345) == False
assert is_Diff(12346) == True
assert is_Diff(12347) == False
assert is_Diff(12348) == True
assert is_Diff(12349) == False
assert is_Diff(12350) == True
assert is_Diff(12351) == False
assert is_Diff(12352) == True
assert is_Diff(12353) == False
assert is_Diff(12354) == True
assert is_Diff(12355) == False
assert is_Diff(12356) == True
assert is_Diff(12357) == False
assert is_Diff(12358) == True
assert is_Diff(12359) == False
assert is_Diff(12360) == True
assert is_Diff(12361) == False
assert is_Diff(12362) == True
assert is_Diff(12363) == False
assert is_Diff(12364) == True
assert is_Diff(12365) == False
assert is_Diff(12366) == True
assert is_Diff(12367) == False
assert is_Diff(12368) == True
assert is_Diff(12369) == False
assert is_Diff(12370) == True
assert is_Diff(12371) == False
assert is_Diff(12372) == True
assert is_Diff(12373) == False
assert is_Diff(12374) == True
assert is_Diff(12375) == False
assert is_Diff(12376) == True
assert is_Diff(12377) == False
assert is_Diff(12378) == True
assert is_Diff(12379) == False
assert is_Diff(12380) == True
assert is_Diff(12381) == False
assert is_Diff(12382) == True
assert is_Diff(12383) == False
assert is_Diff(12384) == True
assert is_Diff(12385) == False
assert is_Diff(12386) == True
assert is_Diff(12387) == False
assert is_Diff(12388) == True
assert is_Diff(12389) == False
assert