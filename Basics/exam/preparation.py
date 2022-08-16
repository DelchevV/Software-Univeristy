paper=5.80
cloth=7.20
glue=1.20

papper_rolls=int(input())
cloth_rolls=int(input())
litres_glue=float(input())
discount_percent=int(input())

total=(papper_rolls*paper) + (cloth_rolls*cloth) + (litres_glue*glue)
total=total-total*(discount_percent/100)
print(f"{total:.3f}")