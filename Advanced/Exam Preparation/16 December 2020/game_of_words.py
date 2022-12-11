text = input()
size = int(input())
matrix = [[ch for ch in input()] for _ in range(size)]
number_of_commands = int(input())
directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}
all_successful_moves = []
start_pos = []
for row in range(size):
    for col in range(size):
        if matrix[row][col] == "P":
            start_pos = [row, col]
            matrix[row][col] = "-"

for _ in range(number_of_commands):
    direction = input()

    r, c = start_pos
    r += directions[direction][0]
    c += directions[direction][1]

    if 0 <= r < size and 0 <= c < size:
        if matrix[r][c] != "-":
            text += matrix[r][c]
            matrix[r][c] = "-"

        start_pos = [r, c]
        all_successful_moves.append([r,c])

    else:
        if len(text) > 0:
            text = text[:-1]
if all_successful_moves:
    r, c = all_successful_moves[-1]
else:
    r,c=start_pos

matrix[r][c] = "P"
print(text)
for row in matrix:
    print("".join(row))
