rows, cols = map(int, input().split())
matrix = []
for row in range(rows):
    matrix.append([i for i in input().split()])

best_square=list()
total_sum = 0
for row in range(rows):
    for col in range(cols):
        first = matrix[row][col]
        if col + 1 < cols:
            second = matrix[row][col + 1]
            if second!=first:
                continue
        else:
            break
        if row + 1 < rows:
            third = matrix[row + 1][col]
            if third!=first:
                continue
        else:
            break
        if row + 1 < rows and col + 1 <= cols:
            forth = matrix[row + 1][col + 1]
            if forth!=first:
                continue
        else:
            break
        total_sum+=1

print(total_sum)
