sequence_of_numbers = input().split()
list_of_numbers = []
sum_by_digits = []
needed_len = 0
final_string = ""
text = input()

for number in sequence_of_numbers:
    list_of_numbers.append(int(number))
for element in list_of_numbers:
    needed_index_for_extraction = 0
    for digit in str(element):
        needed_index_for_extraction += int(digit)
        if len(text) < needed_index_for_extraction:
            needed_index_for_extraction -= len(text)
    final_string += text[needed_index_for_extraction]
    text = text[:needed_index_for_extraction] + text[needed_index_for_extraction + 1:]
print(final_string)
