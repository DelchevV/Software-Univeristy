def reverse_text(text):
    text=list(text)
    for _ in range(len(text)):
        yield text.pop()

for char in reverse_text("step"):
    print(char, end='')
