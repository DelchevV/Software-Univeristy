# You will receive two lines of input:
# •	a list of employees' happiness as a string of numbers separated by a single space
# •	a happiness improvement factor (single number).
# Your task is to find out if the employees are generally happy in their office.
# First, multiply each employee's happiness by the factor.
# Then, print one of the following lines:
# •	If half or more of the employees have happiness greater than or equal to the average:
# "Score: {happy_count}/{total_count}. Employees are happy!"
# •	Otherwise:
# "Score: {happy_count}/{total_count}. Employees are not happy!"

employees_happiness = list(map(int, input().split()))
multiplication_factor = int(input())

employees_happiness_after_factor = [employee * multiplication_factor for employee in employees_happiness]

total_count = len(employees_happiness_after_factor)

average_happiness = sum(employees_happiness_after_factor) / total_count
happy_employees = [happy for happy in employees_happiness_after_factor if happy >= average_happiness]

happy_count = len(happy_employees)
if happy_count >= total_count / 2:
    print(f"Score: {happy_count}/{total_count}. Employees are happy!")
else:
    print(f"Score: {happy_count}/{total_count}. Employees are not happy!")
