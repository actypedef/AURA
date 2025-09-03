"""
Write a function to sort a list of tuples using the second value of each tuple.
assert subject_marks([('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)])==[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
"""
def sort_tuples_by_second_value(tuples_list):
    # Sort the list of tuples based on the second element (marks) in ascending order
    sorted_tuples = sorted(tuples_list, key=lambda x: x[1])
    return sorted_tuples

# Test the function with provided data points
assert sort_tuples_by_second_value([('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]) == [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]