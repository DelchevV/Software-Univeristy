rows=int(input())
matrix=[]
for row in range(rows):
    matrix.append([int(i) for i in input().split(", ")])
result=[]
for row in matrix:
    current_row = []
    for num in row:
        if num%2==0:
            current_row.append(num)
    result.append(current_row)
print(result)