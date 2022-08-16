data = input().split(">")
first_word = data.pop(0)
remaining_power=0
result=[]
for word in data:
    index=data.index(word)
    power_of_explosion=int(word[0])+remaining_power
    if len(word) >= power_of_explosion:
        word=word[power_of_explosion:]
        data[index]=word
        remaining_power=0
    else:
        remaining_power=power_of_explosion-len(word)
        word = ""
        data[index] = word

data.insert(0,first_word)
print(">".join(data))
