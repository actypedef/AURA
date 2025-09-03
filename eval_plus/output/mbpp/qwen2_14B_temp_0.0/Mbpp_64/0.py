"""
Write a function to sort a list of tuples using the second value of each tuple.
assert subject_marks([('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)])==[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
"""
def subject_marks(marks):
    # Sort the list of tuples based on the second item in each tuple
    sorted_list = sorted(marks, key=lambda x: x[1])
    return sorted_list

# Test the function with the provided test case
assert subject_marks([('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]) == [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
