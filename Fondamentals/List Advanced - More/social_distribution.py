population = list(map(int, input().split(", ")))
minimum_wealth = int(input())

distribution = True

still_poor_people = 0
for person in range(len(population)):
    if population[person] < minimum_wealth:
        needed_money = minimum_wealth - population[person]
        # for rich in population:
        richest = max(population)
        index = population.index(richest)
        if population[index] - needed_money < minimum_wealth:
            distribution = False
            print("No equal distribution possible")
            break
        population[index] -= needed_money
        population[person] += needed_money
    for poor in population:
        if poor < minimum_wealth:
            still_poor_people += 1
if distribution:
    print(population)
