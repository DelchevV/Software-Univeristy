size = int(input())
matrix = []
ali_pos = []
directions = {
    "up": (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}
bags = 0
is_escaped = False
for row in range(size):
    line = input().split()
    matrix.append(line)
    if "A" in line:
        ali_pos = [row, line.index("A")]
        matrix[ali_pos[0]][ali_pos[1]] = "*"

while True:
    command = input()
    p1 = ali_pos[0] + directions[command][0]
    p2 = ali_pos[1] + directions[command][1]
    if not (0 <= p1 < size and 0 <= p2 < size):
        break
    else:
        ali_pos = [p1, p2]
        position = matrix[p1][p2]
        matrix[p1][p2] = "*"
        if position == "R":
            break
        if position.isdigit():
            bags += int(position)
        if bags>=10:
            break

if bags >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")
for r in matrix:
    print(*r)
