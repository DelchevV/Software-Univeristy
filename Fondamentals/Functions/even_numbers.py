def even_numbers_filter(number):
    if number%2==0:
        return True
    else:
        return False


list_of_string=input().split(" ")
list_of_numbers=[]
for num in list_of_string:
    list_of_numbers.append(int(num))
even_numbers=filter(even_numbers_filter,list_of_numbers)
list_of_even=list(even_numbers)
print(list_of_even)