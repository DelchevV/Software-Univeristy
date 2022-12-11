rows = 6
matrix = [[ch for ch in input().split()] for _ in range(rows)]
position = input().split(', ')
start = []

for pos in position:
    current_point = ''
    for ch in pos:
        if ch.isdigit():
            current_point += ch
    start.append(int(current_point))

point_1, point_2 = start

moves = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}


def make_move(p1, p2, directions):
    p1 = p1 + moves[directions][0]
    p2 = p2 + moves[directions][1]
    return p1, p2


def create_func(matrix_, values, p1, p2):
    if matrix[p1][p2] == ".":
        matrix[p1][p2] = values
    return matrix_


def update_func(matrix_, values, p1, p2):
    if matrix_[p1][p2].isalnum():
        matrix_[p1][p2] = values
    return matrix_


def delete_func(matrix_, p1, p2):
    matrix_[p1][p2] = "."
    return matrix_


def read_func(matrix_, p1, p2):
    if matrix_[p1][p2].isalnum():
        return print(matrix_[p1][p2])
    return


while True:
    entry = input()
    if entry == "Stop":
        break
    entry = entry.split(', ')
    command = entry[0]
    direction = entry[1]
    point_1, point_2 = make_move(point_1, point_2, direction)
    if command == "Create":
        value = entry[2]
        matrix = create_func(matrix, value, point_1, point_2)

    elif command == "Update":
        value = entry[2]
        matrix = update_func(matrix, value, point_1, point_2)
    elif command == 'Delete':
        matrix = delete_func(matrix, point_1, point_2)
    elif command == "Read":
        read_func(matrix, point_1, point_2)

for row in matrix:
    print(*row)
