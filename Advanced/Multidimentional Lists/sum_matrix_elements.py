rows, cols = map(int, input().split(', '))
matrix=[]
for r in range(rows):
    matrix.append([int(i) for i in input().split(", ")])
total=0
for row in matrix:
    total+=sum(row)
print(total)
print(matrix)

