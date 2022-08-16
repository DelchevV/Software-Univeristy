animal=input()
is_mammmal= animal=="dog"
is_reptile=animal=="crocodile" or animal=="tortoise" or animal=="snake"

if is_mammmal:
    print("mammal")
elif  is_reptile:
    print("reptile")
else:
    print("unknown")