import sys

input_list = input().split()
integer_list = []
start = 0
length = 0
best_start = 0
best_length = 0
number=0
result=""
for item in input_list:
    integer_list.append(int(item))
previous_integer = sys.maxsize
for current_integer in integer_list:
    if current_integer == previous_integer:
        length += 1

        if best_length < length:
            best_length = length
            number = current_integer
    else:
        length = 0
    previous_integer = current_integer
best_length += 1
for num in range(best_length):
    result+=str(number)+" "

print(result[:-1])

