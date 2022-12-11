rows = 6
matrix = [input().split() for _ in range(rows)]
commands = input().split(', ')

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}
start = []
is_suitable = [False, False, False]

for row in range(rows):
    is_found = False

    for col in range(rows):
        if matrix[row][col] == "E":
            start.append(row)
            start.append(col)
            is_found = True
            break

    if is_found:
        break

for command in commands:
    p1, p2 = start
    p1 = p1 + directions[command][0]
    p2 = p2 + directions[command][1]

    if p1 < 0:
        p1 = 5
    elif p1 > 5:
        p1 = 0
    if p2 < 0:
        p2 = 5
    elif p2 > 5:
        p2 = 0

    if matrix[p1][p2] == "W":
        print(f'Water deposit found at ({p1}, {p2})')
        is_suitable[0] = True
    elif matrix[p1][p2] == 'M':
        print(f'Metal deposit found at ({p1}, {p2})')
        is_suitable[1] = True
    elif matrix[p1][p2] == "C":
        print(f'Concrete deposit found at ({p1}, {p2})')
        is_suitable[2] = True
    elif matrix[p1][p2] == "R":
        print(f"Rover got broken at ({p1}, {p2})")
        break

    start = [p1, p2]

if all(is_suitable):
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
