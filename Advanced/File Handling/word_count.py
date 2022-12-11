import re

searched_words = {}

with open('sources/words.txt', 'r') as file:
    for line in file:
        words = line.split()
        for word in words:
            searched_words[word] = 0

pattern = r'[A-Za-z]+'
with open('sources/input.txt', 'r') as file:
    result = re.findall(pattern, file.read())

    for key in searched_words:
        for res in result:
            if key.lower() == res.lower():
                searched_words[key] += 1

with open('sources/output.txt', 'w') as writer:
    final_result = sorted(searched_words.items(), key=lambda x: -x[1])
    for final in final_result:
        writer.write(f'{final[0]}-{final[1]}\n')
