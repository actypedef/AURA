"""
The input is given as - a dictionary with a student name as a key and a tuple of float (student_height, student_weight) as a value, - minimal height, - minimal weight. Write a function to filter students that have height and weight above the minimum.
assert filter_data({'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)},6.0,70)=={'Cierra Vega': (6.2, 70)}
"""
def filter_data(students, min_height, min_weight):
    # Initialize an empty dictionary to store filtered results
    result = {}
    
    # Iterate through each student in the input dictionary
    for student, data in students.items():
        # Check if the student's height and weight meet or exceed the minimum requirements
        if data[0] >= min_height and data[1] >= min_weight:
            # If criteria met, add the student to the result dictionary
            result[student] = data
    
    # Return the filtered dictionary containing only students meeting the criteria
    return result

# Test the function with provided data points
assert filter_data({'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}, 6.0, 70) == {'Cierra Vega': (6.2, 70)}