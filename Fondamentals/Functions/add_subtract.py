def sum_numbers(a,b):
    result=a+b
    return result


def subtract(c):
    result=c
    return result


def add_nad_subtract(a,b,c):
    result=sum_numbers(a,b)-subtract(c)
    return result


first_num=int(input())
second_num=int(input())
third_num=int(input())
print(add_nad_subtract(first_num,second_num,third_num))