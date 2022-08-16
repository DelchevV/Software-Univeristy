message=input()


def move_func(messages, letters):
    messages=message[letters:]+message[:letters]
    return messages


def insert_func(messages, indexes, values):
    messages=message[:indexes]+values+message[indexes:]
    return messages


def change_func(messages, subst, repl):
    messages=messages.replace(subst,repl)
    return messages


while True:
    entry=input().split("|")
    command=entry[0]
    if command=="Decode":
        break
    if command=="Move":
        letters_num = int(entry[1])
        message = move_func(message, letters_num)
    elif command=="Insert":
        index = int(entry[1])
        value = entry[2]
        message = insert_func(message, index, value)
    elif command=="ChangeAll":
        substring=entry[1]
        replacement=entry[2]
        message=change_func(message,substring,replacement)
print(f"The decrypted message is: {message}")