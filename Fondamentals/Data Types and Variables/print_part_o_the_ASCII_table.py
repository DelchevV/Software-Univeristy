starting_chr=int(input())
ending_chr=int(input())
for current_chr in range(starting_chr, ending_chr+1):
    character=chr(current_chr)
    print(character , end=" ")