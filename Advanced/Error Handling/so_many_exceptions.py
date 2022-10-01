numbers_list = list(map(int,input().split(", ")))
result = 1

for num in numbers_list:
    if num <= 5:
        result *= num
    elif num <= 10:
        result /= num

print(result)
