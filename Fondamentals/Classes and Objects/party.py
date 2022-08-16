class Party:
    def __init__(self):
        self.people=[]


party=Party()
while True:
    data=input()
    if data=="End":
        break
    party.people.append(data)
print("Going: "+", ".join(party.people))
print("Total: "+ str(len(party.people)))
