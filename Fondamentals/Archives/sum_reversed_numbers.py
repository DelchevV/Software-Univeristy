list_of_string=input().split()
integer_list=[int(string) for string in list_of_string]
string_of_calculation=""
sum_list=[]
for number in integer_list:
    reversed_num = 0
    while number != 0:
        digit = number % 10
        reversed_num = reversed_num * 10 + digit
        number //= 10
    string_of_calculation+=str(reversed_num) + " + "
    sum_list.append(reversed_num)
print(sum(sum_list))