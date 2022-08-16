string_list = input().split()
integer_list = []
command=input()
command_list = command.split()
operation = ""
item = 0
position = 0
even_string=""
odd_string=""
is_even=True
for i in string_list:
    integer_list.append(int(i))
while command_list[0] != "Odd" or command_list[0] != "Even":
    if command_list[0]=="Odd" or command_list[0]=="Even":
        if command_list[0]=="Odd":
            is_even=False
        break
    for element in range(len(command_list)):
        if command_list[0] == "Delete":
            operation = "Delete"
            item = int(command_list[-1])
        elif command_list[0] == "Insert":
            operation = "Insert"
            item = int(command_list[1])
            position = int(command_list[-1])
    if operation == "Delete":
        for upcoming_delete in integer_list:
            if upcoming_delete==item:
                integer_list.remove(upcoming_delete)
    elif operation=="Insert":
        integer_list.insert(position,item)
    command = input()
    command_list = command.split()


for even in integer_list:
    if even%2==0:
        even_string+=str(even)+" "
    else:
        odd_string+=str(even)+" "
if is_even:
    print(even_string[:-1])
else:
    print(odd_string[:-1])



