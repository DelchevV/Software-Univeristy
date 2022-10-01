rows=int(input())
commands=input().split()
matrix=[]
for row in range(rows):
    matrix.append([i for i in input().split()])
start_position=[]
total_coal=0
for row in range(rows):
    for col in range(rows):
        if matrix[row][col]=="s":
            start_position.append(row)
            start_position.append(col)
        if matrix[row][col] == "c":
            total_coal+=1
found_coal=0
is_game_over=False

for command in commands:
    p1,p2=start_position
    if command=="left":
        if p2-1>=0:
            p2-=1
        else:
            continue
    elif command=="right":
        if p2+1<rows:
            p2+=1
        else:
            continue
    elif command=="up":
        if p1 -1 >=0:
            p1-=1
        else:
            continue
    elif command=='down':
        if p1 + 1 < rows:
            p1+=1
        else:
            continue

    if matrix[p1][p2]=='e':
        is_game_over=True
        print(f'Game over! ({p1}, {p2})')
        break
    elif matrix[p1][p2]=='c':
        found_coal+=1
        matrix[p1][p2]='*'
        if found_coal==total_coal:
            print(f'You collected all coal! ({p1}, {p2})')
    start_position=[p1,p2]

if found_coal!=total_coal and  not is_game_over:
    print(f'{total_coal-found_coal} pieces of coal left. ({start_position[0]}, {start_position[1]})')
