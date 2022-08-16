word=input()
reverse_word=""
for r in range(len(word) -1,-1,-1):
    reverse_word+=word[r]
print(reverse_word)