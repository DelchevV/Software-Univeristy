first_number=int(input())
second_number=int(input())
for current in range(first_number,second_number+1):
    odd = 0
    even = 0
    current_num_as_string=str(current)
    for index, digit in enumerate(current_num_as_string):
        if index%2==0:
            odd+=int(digit)
        else:
            even+=int(digit)
    if odd==even:
        print(current, end=" ")

