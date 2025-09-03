"""
Write a function to sort a list of tuples using the second value of each tuple.
assert subject_marks([('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)])==[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
"""
def subject_marks(tuples_list):
    return sorted(tuples_list, key=lambda x: x[1])

# Test cases
assert subject_marks([('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]) == [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
assert subject_marks([('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82), ('History', 75)]) == [('History', 75), ('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
assert subject_marks([('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82), ('History', 75), ('Geography', 85)]) == [('History', 75), ('Social sciences', 82), ('Geography', 85), ('English', 88), ('Science', 90), ('Maths', 97)]