command=input()
first_string=command
while command != "End":
    if command=="SoftUni":
        command = input()
        first_string = command
        continue
    for string in range(len(command)):
        final_string=first_string[string]+first_string[string]
        print(final_string, end='')
    print()
    command=input()
    first_string = command
