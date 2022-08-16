list_of_strings=input().split()
searched_items=input().split()
list_of_integers=[int(num) for num in list_of_strings]
list_of_searched_items=[int(num) for num in searched_items]
taken_numbers=list_of_searched_items[0]
deleted_numbers=list_of_searched_items[1]
searched_number=list_of_searched_items[2]
list_after_extraction=[]
for number in range(taken_numbers):
    list_after_extraction.append(list_of_integers[number])
for number in range(deleted_numbers):
    del list_after_extraction[0]

if searched_number in list_after_extraction:
    print("YES!")
else:
    print("NO!")

