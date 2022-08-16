entry = input().split()
first_word = entry[0]
second_word = entry[1]
result = 0

if len(entry[0]) < len(entry[1]):
    shortest_word = len(entry[0])
else:
    shortest_word = len(entry[1])

while True:
    if len(second_word) == 0 or len(first_word) == 0:
        break
    for i in range(shortest_word):
        result += ord(first_word[0]) * ord(second_word[0])
        first_word = first_word[1:]
        second_word = second_word[1:]

if len(first_word) > 0:
    for i in range(len(first_word)):
        result += ord(first_word[0])
        first_word = first_word[1:]
if len(second_word) > 0:
    for i in range(len(second_word)):
        result += ord(second_word[0])
        second_word = second_word[1:]
print(result)

