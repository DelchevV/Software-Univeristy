import sys

input_line=input()
min=-sys.maxsize
while input_line!="Stop":
    if int(input_line)>min:
        min=int(input_line)
    input_line = input()
print(min)