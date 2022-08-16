import math
import sys

vowel = 'aeiouAEIOU'
command=input()
powerfull_word_points=-sys.maxsize
powerfull_word=""
while command!="End of words":
    points=0
    for character in command:

        points+=ord(character)
    if command[0] in vowel:
        points*=len(command)
        points = math.floor(points)
    else:
            points/=len(command)
            points=math.floor(points)
    if points>powerfull_word_points:
        powerfull_word_points=points
        powerfull_word=command

    command = input()
print(f"The most powerful word is {powerfull_word} - {powerfull_word_points}" )