def banned(banned_word, entry):
    for ban in banned_word:
        if ban in entry:
            entry=entry.replace(ban, "*" * len(ban))
    return entry


banned_words=input().split(", ")
text=input()
print(banned(banned_words,text))

