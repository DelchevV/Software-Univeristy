starting_letter=ord(input())
ending_letter=ord(input())
missing_letter=ord(input())
counter=0

for i1 in range(starting_letter,ending_letter+1):
    for i2 in range(starting_letter,ending_letter+1):
        for i3 in range(starting_letter,ending_letter+1):
            if i1!=missing_letter and i2!=missing_letter and i3!=missing_letter:
                print(f"{chr(i1)}{chr(i2)}{chr(i3)}",end=" ")
                counter+=1
print(counter)