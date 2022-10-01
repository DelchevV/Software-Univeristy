from sys import maxsize

rows, cols = list(map(int, input().split()))
matrix = []
for row in range(rows):
    matrix.append([int(i) for i in input().split()])
biggest_sum = -maxsize
biggest_square = []

for row in range(rows-2):
    for col in range(cols-2):
        current_sum = 0

        x3_square = [
            [matrix[row][col], matrix[row][col + 1], matrix[row][col + 2]],
            [matrix[row + 1][col], matrix[row + 1][col + 1], matrix[row + 1][col + 2]],
            [matrix[row + 2][col], matrix[row + 2][col + 1], matrix[row + 2][col + 2]]
        ]
        for r in x3_square:
            current_sum += sum(r)
        if current_sum > biggest_sum:
            biggest_sum = current_sum
            biggest_square = x3_square

print(f'Sum = {biggest_sum}')
for row in biggest_square:
    print(" ".join(map(str,row)))
