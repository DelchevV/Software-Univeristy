punctuation_symbols=["-", ",", ".", "!", "?","'"]
final_text=[]
with open('sources/even_lines.txt') as file:
    text=file.readlines()
    
    counter=1
    for line in range(len(text)):
        letters=0
        punctuations=0

        for ch in text[line]:
            if ch.isalpha():
                letters+=1
            if ch in punctuation_symbols:
                punctuations+=1

        final_text.append(f'Line {counter}: {text[line].strip()} ({letters})({punctuations})')
        counter+=1

with open('sources/output.txt','w') as writer:
    for row in final_text:
        writer.write(row+'\n')