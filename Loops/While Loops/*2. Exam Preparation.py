failed_threshold = int(input())
failed_times = 0
number_solved_problems = 0
grades_sum = 0
last_task = ""
has_failed = True

while failed_times < failed_threshold:
    problem_name = input()
    if problem_name == "Enough":
        has_failed = False
        break
    grade = int(input())
    if grade <= 4:
        failed_times += 1
    grades_sum += grade
    number_solved_problems += 1
    last_task = problem_name

if has_failed:
    print(f"You need a break, {failed_threshold} poor grades.")
else:
    print(f"Average score: {grades_sum / number_solved_problems:.2f}")
    print(f"Number of problems: {number_solved_problems}")
    print(f"Last problem: {last_task}")