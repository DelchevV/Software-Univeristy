string=input()


def translate(text,ch, replacement):
    text=text.replace(ch,replacement)
    print(text)
    return text


def includes(subst,text):
    if subst in text:
        print("True")
    else:
        print("False")
    return text


def start(subst,text):
    return print(text.startswith(subst))


def lowercase(text):
    text=text.lower()
    print(text)
    return text


def find_index(ch,text):
    return print(text.rfind(ch))


def remove_func(start,count,text):
    text=text[:start]+text[count+start:]
    print(text)
    return text

while True:
    entry=input().split()
    command=entry[0]
    if command=="End":
        break
    if command=="Translate":
        ch=entry[1]
        replacement=entry[2]
        string=translate(string,ch,replacement)
    elif command=="Includes":
        substring=entry[1]
        string=includes(substring,string)
    elif command=="Start":
        substring=entry[1]
        start(substring,string)
    elif command=="Lowercase":
        string=lowercase(string)
    elif command=="FindIndex":
        ch=entry[1]
        find_index(ch,string)
    elif command=="Remove":
        start_index=int(entry[1])
        count=int(entry[2])
        string=remove_func(start_index,count,string)