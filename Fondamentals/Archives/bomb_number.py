sequence = input().split()
command = input().split()
bomb = int(command[0])
power = int(command[1])
bomb_index = 0
integer_list = [int(string) for string in sequence]
for num in range(len(integer_list)):
    if bomb == integer_list[num]:
        bomb_index = num
        break
start_bombing=bomb_index-power
bombing_len=0

for number in range(power*2+1):
    integer_list.remove(integer_list[start_bombing])
print(sum(integer_list))
