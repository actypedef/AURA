"""
Write a function to count bidirectional tuple pairs.
assert count_bidirectional([(5, 6), (1, 2), (6, 5), (9, 1), (6, 5), (2, 1)] ) == 3
"""
def count_bidirectional(tuples_list):
    # Create a set of all elements from both tuples
    all_elements = {element for tup in tuples_list for element in tup}
    
    # Count the number of unique pairs where each pair consists of two different elements
    bidirectional_pairs_count = sum(1 for i in range(len(all_elements)) for j in range(i+1, len(all_elements)) if (all_elements[i], all_elements[j]) in tuples_list or (all_elements[j], all_elements[i]) in tuples_list)
    
    return bidirectional_pairs_count

# Test the function
assert count_bidirectional([(5, 6), (1, 2), (6, 5), (9, 1), (6, 5), (2, 1)]) == 3