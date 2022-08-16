# SoftUni just got a new fancy parking lot. It even has online parking validation, except the online service doesn't work. It can only receive users' data, but it doesn't know what to do with it. Good thing you're on the dev team and know how to fix it, right?
# Write a program, which validates a parking place - users can register to enter the park and unregister to leave.
# The program receives 2 types of commands:
# •	"register {username} {license_plate_number}":
# o	The system only supports one car per user at the moment, so if a user tries to register another license plate using the same username, the system should print:
# "ERROR: already registered with plate number {license_plate_number}"
# o	If the check above passes successfully, the user should be registered, so the system should print:
#  "{username} registered {license_plate_number} successfully"
# •	"unregister {username}":
# o	If the user is not present in the database, the system should print:
# "ERROR: user {username} not found"
# o	If the check above passes successfully, the system should print:
# "{username} unregistered successfully"
# After you execute all the commands, print all the currently registered users and their license plates in the format:
# •	"{username} => {license_plate_number}"


number_of_commands = int(input())
parking_validator = {}
for num in range(number_of_commands):
    data = input().split()
    command = data[0]
    name = data[1]
    if command == "register":
        license_plate = data[2]
        if name not in parking_validator:
            parking_validator[name] = license_plate
            print(f"{name} registered {license_plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {license_plate}")
    elif command == "unregister":
        if name not in parking_validator:
            print(f"ERROR: user {name} not found")
        else:
            del parking_validator[name]
            print(f"{name} unregistered successfully")
for key, value in parking_validator.items():
    print(f"{key} => {value}")
