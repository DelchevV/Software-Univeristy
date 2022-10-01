rows, cols = tuple(map(int, input().split()))
matrix = []
for row in range(rows):
    current_row = input()
    matrix.append([ch for ch in current_row])

raw_command = input()
commands = [ch for ch in raw_command]
start_pos = []
for row in range(rows):
    is_found = False
    for col in range(cols):
        if matrix[row][col] == "P":
            start_pos.append(row)
            start_pos.append(col)
            is_found = True
            break
    if is_found:
        break

for command in commands:
    p1, p2 = start_pos
    if command == "L":
        if p2 - 1 >= 0:
            p2 -= 1
        else:
            print(f'won: {p1} {p2}')
            break
    elif command == "R":
        if p2 + 1 < rows:
            p2 += 1
        else:
            print(f'won: {p1} {p2}')
            break
    elif command == "U":
        if p1 - 1 >= 0:
            p1 -= 1
        else:
            print(f'won: {p1} {p2}')
            break
    elif command == 'D':
        if p1 + 1 < rows:
            p1 += 1
        else:
            print(f'won: {p1} {p2}')
            break
    copy_matrix = matrix.copy()
    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == "B":

                b_p1 = row
                b_p2 = col
                if b_p1 - 1 >= 0:
                    copy_matrix[b_p1 - 1][b_p2] = "B"
                if b_p1 + 1 < rows:
                    copy_matrix[b_p1 + 1][b_p2] = "B"
                if b_p2-1 >= 0:
                    copy_matrix[b_p1][b_p2 - 1] = "B"
                if b_p2+1 < cols:
                    copy_matrix[b_p1][b_p2 + 1] = "B"
    matrix=copy_matrix

    is_dead = False
    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == "B" and row == p1 and col == p2:
                print(f'dead: {p1} {p2}')
                is_dead=True
                break
        if is_dead:
            break
    if is_dead:
        break
    start_pos = [p1, p2]
for r in matrix:
    print(*r)


