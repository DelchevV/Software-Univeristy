head=input()
body=input()
tail=input()
animal=[head, body, tail]
animal[0], animal[-1]=animal[-1],animal[0]
print(animal)