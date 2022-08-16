number_of_row=int(input())
matrix=[]
for row in range(number_of_row):
    current_row=list(map(int,input().split()))
    matrix.append(current_row)
data=input().split()

for attack in range(len(data)):
    # print(data[attack])

    current_command=data[attack].split("-")
    current_row=current_command[0]
    current_column=current_command[1]

    # print(current_row)
    # print(current_column)



# print(matrix[0])
# print(matrix[1])
# print(matrix[2])