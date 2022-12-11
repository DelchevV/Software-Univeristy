import math

size = int(input())
matrix = [input().split() for _ in range(size)]
directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}
start_pos = []
all_positions = [start_pos]
coins = 0
not_a_coin = ["P", "X", "."]

for row in range(size):
    for col in range(size):
        if matrix[row][col] == "P":
            start_pos.append(row)
            start_pos.append(col)

while True:
    direction = input()
    p1, p2 = start_pos
    p1 += directions[direction][0]
    p2 += directions[direction][1]
    if p1 < 0:
        p1 = size - 1
    elif p1 > size - 1:
        p1 = 0

    if p2 < 0:
        p2 = size - 1
    elif p2 > size - 1:
        p2 = 0

    start_pos = [p1, p2]
    all_positions.append(start_pos)

    if matrix[p1][p2] not in not_a_coin:
        coins += int(matrix[p1][p2])
        matrix[p1][p2] = '.'

    elif matrix[p1][p2] == "X":
        print(f"Game over! You've collected {math.floor(coins / 2)} coins.")
        break

    if coins >= 100:
        print(f"You won! You've collected {coins} coins.")
        break

print('Your path:')
print(*all_positions, sep="\n")
