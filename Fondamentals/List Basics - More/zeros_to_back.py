string_list = list(input().split(", "))
digit_list = []
zeros_list = []
for string in string_list:
    digit_list.append(int(string))
for digit in digit_list:
    if digit==0:
        zeros_list.append(0)
for item in range(len(digit_list)):
    if 0 in digit_list:
        digit_list.remove(0)


final_list = digit_list + zeros_list
print(final_list)
