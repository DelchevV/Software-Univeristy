rows=int(input())
matrix=[]
for row in range(rows):
    matrix.append([int(i) for i in input().split()])
primary_diagonal=[]
secondary_diagonal=[]
for row in range(rows):
    primary_diagonal.append(matrix[row][row])
counter=1
for row in range(rows):
    secondary_diagonal.append(matrix[row][rows-counter])
    counter+=1
prime_sum=sum(primary_diagonal)
secondary_sum=sum(secondary_diagonal)
print(abs(prime_sum-secondary_sum))