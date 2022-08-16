contest_pass={}
submission_info={}
while True:
    data=input()
    if data=="end of contests":
        break
    data=data.split(":")
    contest=data[0]
    password=data[1]
    contest_pass[contest]=password


def is_valid_contest(contests,contest_dict):
    is_valid=False
    if contests in contest_dict:
        is_valid=True
    return is_valid


def is_valid_pass(passwords, contest_dict):
    is_valid=False
    if passwords in contest_dict.values():
        is_valid=True
    return is_valid

def is_user_exist(user, submission_dict):
    exists=False
    for item in submission_dict.values():
        if user == item:
            exists=True
        return exists

def is_contest_exist_for_user(user, contests, submission_dict):
    exist=False
    for item in submission_dict[user]:
        if contests ==item:
            exist=True
        return exist


while True:
    data=input()
    if data=="end of submissions":
        break
    data=data.split("=>")
    contest=data[0]
    password=data[1]
    username=data[2]
    points=data[3]
    if is_valid_contest(contest,contest_pass) and is_valid_pass(password,contest_pass):
        if username not in submission_info:
            submission_info[username]=[contest,points]
        elif is_contest_exist_for_user(username,contest_pass,submission_info) and is_user_exist(username,submission_info):
            for item in submission_info[username]:
                if item==contest:
                    pass

print(contest_pass)
print(submission_info)