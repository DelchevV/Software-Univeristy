list_of_string = input().split(" ")
numbers = []
for string in list_of_string:
    numbers.append(int(string))
numbers.sort()
print(numbers)

