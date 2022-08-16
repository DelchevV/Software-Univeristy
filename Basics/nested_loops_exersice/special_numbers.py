number=int(input())
is_special=True
for i in range(1111,9999+1):
    number_in_string=str(i)
    for index, digit in enumerate(number_in_string):
        if int(digit)!=0:
            if number%int(digit)!=0:
                is_special=False
                break
            else:
                is_special=True
        else:
            is_special=False
            break
    if is_special:
        print(f"{i} ", end="")