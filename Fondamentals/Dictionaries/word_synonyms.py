num = int(input())
synonyms_dict = {}
for lap in range(num):
    word = input()
    synonym = input()
    if word in synonyms_dict.keys():
        synonyms_dict[word] +=", " + synonym
    else:
        synonyms_dict[word]=synonym
for ele in synonyms_dict:
    print(ele + " - " + synonyms_dict[ele])