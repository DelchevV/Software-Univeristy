class DecorationRepository:
    def __init__(self):
        self.decorations = []

    def add(self, decoration):
        self.decorations.append(decoration)

    def remove(self, decoration):
        self.decorations.remove(decoration)

    def find_by_type(self, decoration_type: str):
        for dec in self.decorations:
            if type(dec).__name__ == decoration_type:
                return dec

        return "None"


