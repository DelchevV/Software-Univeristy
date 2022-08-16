sums_list_as_string=input().split(", ")
beggars=int(input())
index_counter=0
sums_list_as_digits=[]
final_sums_of_beggars=[]
for money in range(len(sums_list_as_string)):
    sums_list_as_digits.append(int(sums_list_as_string[money]))
while index_counter<beggars:
    current_beggar_profit = 0
    for current_index in range(index_counter,len(sums_list_as_digits),beggars):
        current_beggar_profit+=sums_list_as_digits[current_index]
    index_counter+=1
    final_sums_of_beggars.append(current_beggar_profit)
print(final_sums_of_beggars)