def calculations(parameter, first_num, second_num):
    result=0
    if parameter=="multiply":
        result=first_num*second_num
    elif parameter=="divide":
        result=first_num/second_num
    elif parameter=="add":
        result=first_num+second_num
    elif parameter=="subtract":
        result=first_num-second_num
    return int(result)

paramter=input()
first_num=int(input())
second_num=int(input())
print(calculations(paramter,first_num,second_num))