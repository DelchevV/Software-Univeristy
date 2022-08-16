contest_add = input()

exams_information = {"contest": {}, "students": {}}
contest_d, students_d = "contest", "students"

while contest_add != "end of contests":
    contest, contest_pass = contest_add.split(":")
    exams_information[contest_d][contest] = contest_pass
    contest_add = input()

submissions = input()
while submissions != "end of submissions":
    contest, contest_pass, contest_user, contest_points = [int(x) if x.isdigit() else x for x in submissions.split("=>")]
    if contest in exams_information[contest_d] and exams_information[contest_d][contest] == contest_pass:
        exams_information[students_d][contest_user] = exams_information[students_d].get(contest_user, {})
        exams_information[students_d][contest_user][contest] = exams_information[students_d][contest_user].get(contest, 0)
        if exams_information[students_d][contest_user][contest] < contest_points:
            exams_information[students_d][contest_user][contest] = contest_points
    submissions = input()
print(exams_information)