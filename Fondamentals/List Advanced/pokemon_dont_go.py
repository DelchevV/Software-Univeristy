# Ely likes to play Pokemon Go a lot. But Pokemon Go bankrupted… So the developers made Pokemon Don't Go out of depression. And so Ely now plays Pokemon Don't Go. In Pokemon Don't Go, when you walk to a certain pokemon, those closest to you naturally get further, and those further from you, get closer.
# You will receive a sequence of integers, separated by spaces - the distances to the pokemon. Then you will begin receiving integers, which will correspond to indexes in that sequence.
# When you receive an index, you must remove the element at that index from the sequence (as if you've captured the pokemon).
# •	You must increase the value of all elements in the sequence which are less or equal to the removed element with the value of the removed element.
# •	You must decrease the value of all elements in the sequence which are greater than the removed element with the value of the removed element.
# If the given index is less than 0, remove the first element of the sequence, and copy the last element to its place.
# If the given index is greater than the last index of the sequence, remove the last element from the sequence, and copy the first element to its place.
# The increasing and decreasing elements should also be done in these cases. The element whose value you should use is the removed element.
# The program ends when the sequence has no elements (there are no pokemon left for Ely to catch).
def increase_decrease_func(numb, removed):
    for element in range(len(numb)):
        if numb[element] <= removed:
            numb[element] += removed
        elif numb[element] > removed_number:
            numb[element] -= removed


sum_of_removed = 0
numbers = list(map(int, input().split()))
while True:
    if len(numbers) <= 0:
        break
    removed_number = 0
    index = int(input())
    if len(numbers) > index >= 0:
        removed_number = numbers.pop(index)
        increase_decrease_func(numbers, removed_number)
    elif index < 0:
        removed_number = numbers[0]
        increase_decrease_func(numbers, removed_number)
        numbers[0] = numbers[-1]
    elif index >= len(numbers):
        removed_number = numbers[-1]
        if len(numbers) > 1:
            increase_decrease_func(numbers, removed_number)
            numbers[-1] = numbers[0]

    sum_of_removed += removed_number

print(sum_of_removed)
