class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = list(sequence)
        self.number = number

    def __iter__(self):
        return self

    def __next__(self):
        if self.number<=0:
            raise StopIteration
        self.number-=1
        current_ch=self.sequence.pop(0)
        self.sequence.append(current_ch)
        return current_ch

result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end ='')


