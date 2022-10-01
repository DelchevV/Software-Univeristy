rows=int(input())
matrix=[]
for row in range(rows):
    matrix.append([int(i)  for i in input().split()])


def is_valid_func(command_info, matrix_rows):
    command_info=command_info[1:]
    p1=int(command_info[0])
    p2=int(command_info[1])
    if 0 <= p1 < matrix_rows and 0 <= p2 < matrix_rows:
        return True
    else:
        return False


while True:
    command=input()
    if command=="END":
        break
    command=command.split()
    p1 = int(command[1])
    p2 = int(command[2])
    if command[0]=="Add":
        if 0 <= p1 < rows and 0 <= p2 < rows:
            p1,p2=int(command[1]),int(command[2])
            matrix[p1][p2]+=int(command[3])
        else:
            print("Invalid coordinates")
    elif command[0]=="Subtract":
        if 0 <= p1 < rows and 0 <= p2 < rows:
            p1, p2 = int(command[1]), int(command[2])
            matrix[p1][p2] -= int(command[3])
        else:
            print("Invalid coordinates")

for r in matrix:
    print(*r)
