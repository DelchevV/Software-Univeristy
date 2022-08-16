data = input().split()
data_dict = {}
odd = []
for ele in data:
    key = ele.lower()
    if key not in data_dict:
        data_dict[key] = 1
    else:
        data_dict[key] += 1
for (key, value) in data_dict.items():
    if value % 2 != 0:
        print(key, end=" ")

# for ele in data_dict:
#     if data_dict[ele]%2!=0:
#         odd.append(ele)
# print(" ".join(odd))
