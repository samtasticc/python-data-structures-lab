# ------ EXERCISE 1

# Exercise 1: List and Indexing
#
# Create a list named students containing at least three student names (strings).
# Assign the second student’s name to a variable named first_student.
# Assign the last student’s name to a variable named last_student.

# students = ['Eric', 'Dee', 'Sam']
# def manage_students():
#     # your code here
#     first_student = students[0]
#     last_student = students[-1]
#     return (f"First student: {first_student}, Last student: {last_student}")
# # Call the function and print the result
# print('Exercise 1:', manage_students())

# ------ EXERCISE 2

# Exercise 2: Loop and String Concatenation
#
# Create a tuple named foods containing the same number of foods (strings) as there are names in the students list.
# Create a variable named meal and assign an empty string to it.
# Use a for loop to iterate over the strings in foods and append each string to meal.

foods = ('quinoa', 'broccoli', 'english muffins')
def combine_foods():
    # your code here
    meal = ' '
    for food in foods:
        meal += food + ' '
    return meal

# Call the function and print the result
print('Exercise 2:', combine_foods())
