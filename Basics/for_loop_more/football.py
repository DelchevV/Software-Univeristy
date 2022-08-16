capacity=int(input())
fans=int(input())
sector_a=0
sector_b=0
sector_v=0
sector_g=0
for i in range(fans):
    sector=input()
    if sector=="A":
        sector_a+=1
    elif sector=="B":
        sector_b += 1
    elif sector=="V":
        sector_v += 1
    elif sector=="G":
        sector_g += 1

print(f"{sector_a/fans*100:.2f}%")
print(f"{sector_b/fans*100:.2f}%")
print(f"{sector_v/fans*100:.2f}%")
print(f"{sector_g/fans*100:.2f}%")
print(f"{fans / capacity * 100:.2f}%")