student_name = input()
current_year_grade = 0
grades = 0
average_grades = 0
failed_grades = 0
failed_year = 0
class_year = 1

while class_year <= 12:
    current_year_grade = float(input())

    if current_year_grade >= 4.00:
        class_year += 1
        grades+= current_year_grade
    else:
        failed_year += 1
        if failed_year > 1:
            break

average_grades = grades / 12

if class_year >= 12:
    print(f"{student_name} graduated. Average grade: {average_grades:.2f}")
else:
    print(f"{student_name} has been excluded at {class_year} grade")
