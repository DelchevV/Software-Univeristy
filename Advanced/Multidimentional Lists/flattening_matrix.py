rows=int(input())
matrix=[]
for row in range(rows):
    matrix.append([int(i) for i in input().split(', ')])
result=[]
for row in matrix:
    for num in row:
        result.append(num)
print(result)