# Write a program that keeps the information about students and their grades.
# On the first line, you will receive an integer number representing the next pair of rows. On the next lines, you will be receiving each student's name and their grade.
# Keep track of all grades for each student and keep only the students with an average grade higher than or equal to 4.50.
# Print the final dictionary with students and their average grade in the following format:
# "{name} -> {averageGrade}"
# Format the average grade to the 2nd decimal place.


number_of_pairs = int(input())
students = {}

for student in range(number_of_pairs):
    name = input()
    grade = float(input())
    if name not in students:
        students[name] = []
        students[name].append(grade)
    else:
        students[name].append(grade)

for key, value in students.items():
    current_sum = sum(value) / len(value)
    students[key] = current_sum

filtered_marks = {item: value for item, value in students.items() if value >= 4.50}
for key, value in filtered_marks.items():
    print(f"{key} -> {value:.2f}")
