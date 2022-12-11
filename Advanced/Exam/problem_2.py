size = int(input())
racing_num = input()
matrix = [input().split() for _ in range(size)]
passed_km = 0
reached_finish = False

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

start_pos = [0, 0]
while True:
    direction = input()

    if direction == "End":
        break

    row, col = start_pos
    row += directions[direction][0]
    col += directions[direction][1]

    if matrix[row][col] == ".":
        passed_km += 10

    elif matrix[row][col] == "T":
        matrix[row][col] = "."
        passed_km += 30

        for r in range(size):
            is_found = False
            for c in range(size):
                if matrix[r][c] == "T":
                    matrix[r][c] = "."
                    start_pos = [r, c]
                    is_found = True
                    break
            if is_found:
                break

        continue

    elif matrix[row][col] == "F":
        passed_km += 10
        reached_finish = True

    start_pos = [row, col]
    if reached_finish:
        break

matrix[start_pos[0]][start_pos[1]] = "C"

if reached_finish:
    print(f"Racing car {racing_num} finished the stage!")
else:
    print(f"Racing car {racing_num} DNF.")

print(f"Distance covered {passed_km} km." )

for row in matrix:
    print("".join(row))
