quantity=int(input())
days=int(input())
spirit_points=0
ornament_set=2
tree_skirt=5
tree_garland=3
tree_lights=15
total=0
for day in range(1,days+1):
    if day%11==0:
        quantity+=2
    if day%2==0:
        total+=ornament_set*quantity
        spirit_points+=5
    if day%3==0:
        total+=(tree_skirt+tree_garland)*quantity
        spirit_points+=13
    if day%5==0:
        total+=tree_lights*quantity
        spirit_points+=17
        if day%3==0:
            spirit_points+=30
        if day%10==0:
            spirit_points-=20
            total+=tree_lights+tree_garland+tree_skirt
if days%10==0:
    spirit_points-=30
print(f"Total cost: {total}")
print(f"Total spirit: {spirit_points}")