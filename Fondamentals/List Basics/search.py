number_of_strings=int(input())
word=input()
strings=[]
filtered_strings=[]
for string in range(number_of_strings):
    current_string=input()
    strings.append(current_string)
print(strings)
for i in strings:
    if word in i:
        filtered_strings.append(i)
print(filtered_strings)