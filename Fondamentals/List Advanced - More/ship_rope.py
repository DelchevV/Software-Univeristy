input_string=input()
numbers_list=[]
non_numbers_list=[]
take_list=[]
skip_list=[]

for ch in input_string:
    if ch.isdigit():
        numbers_list.append(int(ch))
    else:
        non_numbers_list.append(ch)

for digit in range(len(numbers_list)):
    if digit%2==0:
        take_list.append(numbers_list[digit])
    else:
        skip_list.append(numbers_list[digit])
taken_part=[]
skipped_parts=[]
for index in range(len(take_list)):
    amount_of_taken_ch=take_list[index]
    amount_of_skipped_ch=skip_list[index]
    for ch in range(amount_of_taken_ch):
        if len(non_numbers_list) > 0:
            poped_ch=non_numbers_list.pop(0)
            taken_part.append(poped_ch)
    for ch in range(amount_of_skipped_ch):
        if len(non_numbers_list)>0:
            poped_ch=non_numbers_list.pop(0)
            skipped_parts.append(poped_ch)
print("".join(taken_part))
