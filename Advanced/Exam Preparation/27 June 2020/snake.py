size = int(input())
matrix = [[el for el in input()] for _ in range(size)]

snake_pos = []
burrows = []
food_quantity = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(size):
    for col in range(size):

        if matrix[row][col] == "S":
            snake_pos = [row, col]
            matrix[row][col] = "."
        elif matrix[row][col] == "B":
            burrows.append([row, col])


def snake_movement(r, c, food):
    if matrix[r][c] == "*":
        food += 1

    elif matrix[r][c] == "B":

        for burrow in burrows:
            burrow_r, burrow_col = burrow

            if r == burrow_r and c == burrow_col:
                burrows.remove(burrow)
                matrix[r][c] = "-"
                break

        r, c = burrows[0]
        matrix[burrows[0][0]][burrows[0][1]] = "-"
        burrows.pop()

    matrix[r][c] = "."

    return food, [r, c]


while True:
    direction = input()
    row, col = snake_pos

    if not (0 <= row + directions[direction][0] < size and 0 <= col + directions[direction][1] < size):
        print("Game over!")
        break

    else:
        row += directions[direction][0]
        col += directions[direction][1]
        food_quantity, snake_pos = snake_movement(row, col, food_quantity)

    if food_quantity >= 10:
        matrix[snake_pos[0]][snake_pos[1]] = "S"
        print("You won! You fed the snake.")
        break

print(f'Food eaten: {food_quantity}')
for row in matrix:
    print("".join(row))
