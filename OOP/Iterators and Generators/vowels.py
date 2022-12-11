class vowels:
    VOWELS='AUOEIYauoeyi'

    def __init__(self, text):
        self.text=text
        self.vowels=[ch for ch in text if ch in vowels.VOWELS]

    def __iter__(self):
        return self

    def __next__(self):
        if not self.vowels:
            raise StopIteration

        return self.vowels.pop(0)

my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)


