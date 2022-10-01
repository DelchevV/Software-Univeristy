rows = int(input())

matrix = []
for row in range(rows):
    matrix.append([int(i) for i in input().split()])

bombs = input().split()

for bomb in bombs:
    p1, p2 = list(map(int, bomb.split(',')))
    bomb_value = matrix[p1][p2]
    matrix[p1][p2]=0
    if p1 - 1 >= 0:
        if matrix[p1 - 1][p2] > 0:
            matrix[p1 - 1][p2] -= bomb_value

    if p1 + 1 < rows:
        if matrix[p1 + 1][p2] > 0:
            matrix[p1 + 1][p2] -= bomb_value

    if p2 - 1 >= 0:
        if matrix[p1][p2 - 1] > 0:
            matrix[p1][p2 - 1] -= bomb_value

    if p2 + 1 < rows:
        if  matrix[p1][p2 + 1] > 0:
            matrix[p1][p2 + 1] -= bomb_value

    if p1 - 1 >=0 and p2 - 1 >=0:
        if  matrix[p1 - 1][p2 - 1] > 0:
            matrix[p1 - 1][p2 - 1] -= bomb_value

    if p1 - 1 >=0 and p2 + 1 <rows:
        if  matrix[p1 - 1][p2 + 1]  > 0:
            matrix[p1 - 1][p2 + 1] -= bomb_value

    if p1 + 1 <rows and p2 -1 >=0:
        if  matrix[p1 + 1][p2 - 1]  > 0:
            matrix[p1 + 1][p2 - 1] -= bomb_value

    if p1 + 1 <rows and p2 +1 <rows:
        if  matrix[p1 + 1][p2 + 1]  > 0:
            matrix[p1 + 1][p2 + 1] -= bomb_value
alive_nums=[]
for row in matrix:
    alive_nums.extend([num for num in row if num >0])
print(f"Alive cells: {len(alive_nums)}")
print(f'Sum: {sum(alive_nums)}')
for row in matrix:
    print(*row)