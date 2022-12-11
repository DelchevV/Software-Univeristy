def make_sweeper():
    for r in range(size):
        for c in range(size):
            if matrix[r][c] == "-":
                current_sum = 0
                for direction in directions:
                    if 0 <= r + direction[0] < size and 0 <= c + direction[1] < size:
                        if matrix[r + direction[0]][c + direction[1]] == "*":
                            current_sum += 1
                matrix[r][c] = str(current_sum)


size = int(input())
bombs = int(input())
matrix = []

directions = {
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
    (-1, -1),
    (-1, 1),
    (1, -1),
    (1, 1),

}
for row in range(size):
    current_row = []
    for col in range(size):
        current_row.append('-')
    matrix.append(current_row)

for _ in range(bombs):
    r, c = map(int, input().strip('(').strip(")").split(", "))
    if 0 <= r < size and 0 <= c < size:
        matrix[r][c] = "*"

make_sweeper()

for row in matrix:
    print(" ".join(row))
