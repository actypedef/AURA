
def get_max_triples(n):
    """
    You are given a positive integer n. You have to create an integer array a of length n.
        For each i (1 ≤ i ≤ n), the value of a[i] = i * i - i + 1.
        Return the number of triples (a[i], a[j], a[k]) of a where i < j < k, 
    and a[i] + a[j] + a[k] is a multiple of 3.

    Example :
        Input: n = 5
        Output: 1
        Explanation: 
        a = [1, 3, 7, 13, 21]
        The only valid triple is (1, 7, 13).
    """
from typing import *
from collections import *

def get_max_triples(n):
    # Generate the array a based on the given formula
    a = [i * i - i + 1 for i in range(1, n + 1)]
    
    # Count the number of elements in a that give remainder 0, 1, and 2 when divided by 3
    count_mod_0 = count_mod_1 = count_mod_2 = 0
    for num in a:
        if num % 3 == 0:
            count_mod_0 += 1
        elif num % 3 == 1:
            count_mod_1 += 1
        else:
            count_mod_2 += 1
    
    # Calculate the number of valid triples
    # Case 1: All three numbers have the same remainder when divided by 3
    triples_same_mod = (count_mod_0 * (count_mod_0 - 1) * (count_mod_0 - 2) // 6 +
                        count_mod_1 * (count_mod_1 - 1) * (count_mod_1 - 2) // 6 +
                        count_mod_2 * (count_mod_2 - 1) * (count_mod_2 - 2) // 6)
    
    # Case 2: All three numbers have different remainders when divided by 3
    triples_diff_mod = count_mod_0 * count_mod_1 * count_mod_2
    
    # Total number of valid triples
    total_triples = triples_same_mod + triples_diff_mod
    
    return total_triples

# Test the function with the provided example