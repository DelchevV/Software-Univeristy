# You will be given two sequences of strings, separated by ", ".
# Print a new list containing only the strings from the first input line,
# which are substrings of any string in the second input line.

first_sequence=input().split(", ")
second_sequence=input().split(", ")
list_result=[b for b in first_sequence for a in second_sequence if b in a ]
list_result=list(dict.fromkeys(list_result))


print(list_result)

