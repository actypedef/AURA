"""
Write a function to find the nth number in the newman conway sequence.
assert sequence(10) == 6
"""
def sequence(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        sequence_list = [0, 1, 1]
        for i in range(3, n + 1):
            sequence_list.append(sequence_list[sequence_list[i - 1]] + sequence_list[i - sequence_list[i - 1]])
        return sequence_list[n]

assert sequence(10) == 6