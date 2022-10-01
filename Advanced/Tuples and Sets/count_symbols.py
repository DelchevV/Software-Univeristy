text=input()
unique_ch=set()
all_ch=tuple(x for x in text)
for ch in text:
    unique_ch.add(ch)
for ch in sorted(unique_ch):
    print(f'{ch}: {all_ch.count(ch)} time/s')
