data=input()
emojis=[]
while True:
    if ":" not in data:
        break
    index=data.index(":")
    current_emoji=data[index]+data[index+1]
    emojis.append(current_emoji)
    data=data[index+1:]

print("\n".join(emojis))
