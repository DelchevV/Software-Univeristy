first_string=input()
second_string=input()
left_side=''
right_side=''
last_string=first_string
for index in range(len(first_string)+1):
    left_side=second_string[:index+1]
    right_side=first_string[index+1:]
    current_string=left_side+right_side
    if current_string==last_string:
        continue
    print(current_string)
    last_string=current_string