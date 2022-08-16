# Write a program that keeps the information about companies and their employees.
# You will be receiving company names and an employees' id until you receive the command "End" command. Add each employee to the given company. Keep in mind that a company cannot have two employees with the same id.
# Print the company name and each employee's id in the following format:
# "{company_name}
# -- {id1}
# -- {id2}
# …
# -- {idN}"
#

companies = {}
while True:
    data = input()
    if data == "End":
        break
    data = data.split(" -> ")
    company = data[0]
    employee = data[1]
    if company not in companies:
        companies[company] = []
        companies[company].append(employee)
    else:
        if employee not in companies[company]:
            companies[company].append(employee)

for key, value in companies.items():
    print(key)
    for item in value:
        print(f"-- {item}")
