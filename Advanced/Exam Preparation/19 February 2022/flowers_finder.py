from collections import deque

flowers = {
    'rose': 'rose',
    'tulip': 'tulip',
    'lotus': 'lotus',
    'daffodil': 'daffodil'
}

vowels = deque(input().split())
consonants = list(input().split())
word_found = ''
is_found = False
while vowels and consonants:
    vowel = vowels.popleft()
    consonant = consonants.pop()

    for flower in flowers.keys():
        if vowel in flowers[flower]:
            flowers[flower]=flowers[flower].replace(vowel,'')
        if consonant in flowers[flower]:
            flowers[flower]=flowers[flower].replace(consonant,'')

    for key,value in flowers.items():
        if value == "":
            word_found = key
            is_found = True
            break

    if is_found:
        break


if is_found:
    print(f"Word found: {word_found}")
else:
    print("Cannot find any word!")

if any(vowels):
    print(f"Vowels left: {' '.join(vowels)}")
if any(consonants):
    print(f"Consonants left: {' '.join(consonants)}")