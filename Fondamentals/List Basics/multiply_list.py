factor=int(input())
count=int(input())
factorial_list=[]
for number in range(1,count+1):
    factorial_list.append(number*factor)
print(factorial_list)