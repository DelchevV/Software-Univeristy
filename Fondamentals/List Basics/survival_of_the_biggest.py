raw_list_of_numbers=input().split()
removed_numbers=int(input())
list_of_numbers=[]
list_of_removed_numbers=[]
final_list=[]
string_of_list_of_numbers=""
for number in range(len(raw_list_of_numbers)):
    list_of_numbers.append(int(raw_list_of_numbers[number]))
for number in range(removed_numbers):
    smallest_number=min(list_of_numbers)
    list_of_numbers.remove(smallest_number)
for number in range(len(list_of_numbers)):
    final_list.append(str(list_of_numbers[number]))

for element in final_list:
    string_of_list_of_numbers+=element+", "
final_string=string_of_list_of_numbers[:-2]


print(final_string)


