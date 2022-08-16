string=input()
modified_list=[]
numbers=string.split(" ")
for i in range(len(numbers)):
    numbers[i]=int(numbers[i])
for number in numbers:
        if number<0 or number>0:
            current_numbers=number*-1
        if number==0:
            current_numbers=number
        modified_list.append(current_numbers)
print(modified_list)