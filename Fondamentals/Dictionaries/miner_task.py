# You will be given a sequence of strings, each on a new line until you receive the "stop" command. Every odd line on the console represents a resource (e.g., Gold, Silver, Copper, and so on) and every even - quantity.
# Your task is to collect the resources and print them each on a new line.

miner_dict={}
while True:
    key=input()
    if key=="stop":
        break
    value=int(input())
    if key in miner_dict:
        miner_dict[key]+=value
    else:
        miner_dict[key]=value
for (key,value) in miner_dict.items():
    print(key + " -> "+ str(value))
