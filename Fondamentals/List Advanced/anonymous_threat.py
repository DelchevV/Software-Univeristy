text=input().split()

while True:
    data=input().split()
    command=data[0]
    if command=="3:1":
        break
    elif command=="merge":
        start_index=int(data[1])
        end_index=int(data[-1])
        string = ""
        if end_index>len(text):
            continue
        for element in range(start_index,end_index):
            string+=text[element]
        for element in range(start_index,end_index):
            text.pop(start_index)
        text.insert(start_index,string)
    elif command=="divide":
        index=int(data[1])
        partition=int(data[-1])
        word_for_dividing = str(text[index])
        text.pop(index)

        if len(word_for_dividing)/partition>=1:
            chrs_in_part=len(word_for_dividing)//partition
        else:
            pass

        list_of_new_words=[]

        for ch in range(partition):
            current_part=word_for_dividing[:chrs_in_part]
            word_for_dividing=word_for_dividing[chrs_in_part:]
            list_of_new_words.append(current_part)
            print(current_part)

        words_for_insert=" ".join(list_of_new_words)
        text.insert(index,words_for_insert)

print(" ".join(text))

