# The force users struggle to remember which side is the different force users from because they switch them too often. So you are tasked to create a web application to manage their profiles. You should store information for every unique force user registered in the application.
# You will receive several input lines in one of the following formats:
# "{force_side} | {force_user}"
# "{force_user} -> {force_side}"
# The "force_user" and "force_side" are strings, containing any character.
# If you receive "force_side | force_user":
# •	If there is no such force user and no such force side -> create a new force side and add the force user to the corresponding side.
# •	Only if there is no such force user in any force side -> add the force user to the corresponding side.
# •	If there is such force user already -> skip the command and continue to the next operation.
# If you receive a "force_user -> force_side":
# •	If there is such force user already -> change their side.
# •	If there is no such force user in any force side -> add the force user to the corresponding force side.
# •	If there is no such force user and no such force side -> create new force side and add the force user to the corresponding side.
# •	Then you should print on the console: "{force_user} joins the {force_side} side!".
# You should end your program when you receive the command "Lumpawaroo". At that point, you should print each force side. For each side, print the force users.
# In case there are no force users on a side, you shouldn't print the side information.


force_book = {}


def is_force_user_exist(force_books, user):
    already_exists = False
    for item in force_books:
        if user in force_books[item]:
            already_exists = True
            break
    return already_exists


while True:

    data = input()
    if data == "Lumpawaroo":
        break

    elif " | " in data:
        data = data.split(" | ")
        force_side = data[0]
        force_user = data[1]

        if force_side not in force_book and is_force_user_exist(force_book, force_user) == False:
            force_book[force_side] = []
            force_book[force_side].append(force_user)
        elif is_force_user_exist(force_book, force_user):
            continue
        else:
            force_book[force_side].append(force_user)

    elif " -> " in data:
        data = data.split(" -> ")
        force_user = data[0]
        force_side = data[1]

        if is_force_user_exist(force_book, force_user):

            for key in force_book:
                if force_user in force_book[key]:
                    force_book[key].remove(force_user)

            if force_side not in force_book:
                force_book[force_side] = []
            force_book[force_side].append(force_user)

        elif force_side not in force_book and is_force_user_exist(force_book, force_user) == False:
            force_book[force_side] = []
            force_book[force_side].append(force_user)

        elif not is_force_user_exist(force_book, force_user):
            force_book[force_side].append(force_user)

        print(f"{force_user} joins the {force_side} side!")

for key, value in force_book.items():
    if len(value) == 0:
        continue

    print(f"Side: {key}, Members: {len(value)}")
    for item in value:
        print(f"! {item}")
