
replacements=["-", ",", ".", "!", "?"]
with open('sources/even_lines.txt','r') as file:
    text=file.readlines()

for row in range(0,len(text),2):
    for symbol in replacements:
        text[row]=text[row].replace(symbol,"@")
    print(' '.join(text[row].split()[::-1]))


