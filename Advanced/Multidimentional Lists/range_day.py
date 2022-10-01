def move(direction, steps):
    r = shooter_pos[0] + directions[direction][0] * steps
    c = shooter_pos[1] + directions[direction][1] * steps
    if not (0 <= r < rows and 0 <= c < rows):
        return shooter_pos
    if matrix[r][c] == 'x':
        return shooter_pos
    return [r, c]


def shoot(direction):
    r = shooter_pos[0] + directions[direction][0]
    c = shooter_pos[1] + directions[direction][1]

    while 0 <= r < rows and 0 <= c < rows:
        if matrix[r][c] == "x":
            matrix[r][c] = '.'
            return [r, c]
        r += directions[direction][0]
        c += directions[direction][1]


rows = 5
matrix = []
shooter_pos = []
total_targets = 0
hit_targets = 0
hit_targets_pos = []
directions = {
    "up": (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for row in range(rows):
    line = input().split()
    if "A" in line:
        p1 = row
        p2 = line.index("A")
        shooter_pos = [p1, p2]
    total_targets += line.count("x")
    matrix.append(line)
matrix[shooter_pos[0]][shooter_pos[1]] = '.'

number_of_commands = int(input())

for _ in range(number_of_commands):
    command = input().split()
    if command[0] == "move":
        shooter_pos = move(command[1], int(command[2]))
    elif command[0] == "shoot":
        target_down_pos = shoot(command[1])

        if target_down_pos:
            hit_targets_pos.append(target_down_pos)
            hit_targets += 1

        if hit_targets == total_targets:
            print(f"Training completed! All {total_targets} targets hit.")
            break

if hit_targets < total_targets:
    print(f"Training not completed! {total_targets - hit_targets} targets left.")
if hit_targets_pos:
    for hit in hit_targets_pos:
        print(hit)
