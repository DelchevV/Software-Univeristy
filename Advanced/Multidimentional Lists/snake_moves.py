rows, cols = list(map(int, input().split()))
word = input()
chopped_word = [ch for ch in word]
matrix = []
index = 0
for row in range(rows):
    result = ''
    for col in range(cols):
        result += word[index % len(word)]
        index+=1
    if row%2==0:
        matrix.append(result)
    else:
        matrix.append(result[::-1])
for row in matrix:
    print(row)
