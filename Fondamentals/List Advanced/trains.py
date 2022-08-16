# You will receive a number representing the number of wagons a train has.
# Create a list (train) with the given length containing only zeros.
# Until you receive the command "End", you will receive some of the following commands:
# •	"add {people}" – you should add the number of people in the last wagon
# •	"insert {index} {people}" - you should add the number of people at the given wagon
# •	"leave {index} {people}" - you should remove the number of people from the wagon.
# There will be no case in which the people will be more than the count in the wagon.
# There will be no case in which the index is invalid!
# After you receive the "End" command print the train.

number_of_wagons=int(input())
wagons=[0]*number_of_wagons
while True:
    command=input().split()
    current_command=command[0]
    if current_command=="End":
        break

    if current_command=="add":
        people_to_add=int(command[1])
        wagons[-1]+=people_to_add
    elif current_command=="leave":
        people_to_leave=int(command[-1])
        index_of_leave=int(command[1])
        wagons[index_of_leave]-=people_to_leave
    elif current_command=="insert":
        index_of_insert=int(command[1])
        people_to_insert=int(command[-1])
        wagons[index_of_insert]+=people_to_insert
print(wagons)



