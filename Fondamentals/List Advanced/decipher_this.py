# You are given a secret message you should decipher. To do that, you need to know that in each word:
# •	the second and the last letter are switched (e.g., Holle means Hello)
# •	the first letter is replaced by its character code (e.g., 72 means H)


message = input().split()
new_message = []
final_message = []

for mess in message:
    numbers_string = ""
    alpha_string = ""
    for symbol in mess:
        if symbol.isdigit():
            numbers_string = numbers_string + symbol
        if symbol.isalpha():
            alpha_string = alpha_string + symbol
    first_letter = chr(int(numbers_string))
    new_word = first_letter + alpha_string
    new_message.append(new_word)

for word in new_message:
    temp_reverse = list(word)
    temp_reverse[1], temp_reverse[-1] = temp_reverse[-1], temp_reverse[1]
    modified_word = "".join(temp_reverse)
    final_message.append(modified_word)

print(" ".join(final_message))
