rows, cols = list(map(int, input().split()))
matrix = []
for row in range(rows):
    matrix.append([i for i in input().split()])

while True:
    command = input()
    if command == "END":
        break
    command = command.split()
    if command[0]!='swap' or len(command) != 5:
        print('Invalid input!')
        continue

    points = list(map(int, command[1:]))

    if 0 <= points[0] < rows or 0 <= points[1] < cols or \
            0 <= points[2] < rows or 0 <= points[3] < cols:
        points = list(map(int, command[1:]))
        p1, p2 = matrix[points[0]][points[1]], matrix[points[2]][points[3]]
        matrix[points[0]][points[1]] = p2
        matrix[points[2]][points[3]] = p1
        for row in matrix:
            print(*row)
    else:
        print('Invalid input!')

