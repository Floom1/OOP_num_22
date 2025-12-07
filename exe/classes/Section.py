class Section:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.jury = []

    def add_jury(self, jury):
        self.jury.append(jury)

    def get_jury(self):
        if self.jury == []:
            return "Пусто"
        a = ""
        for x in self.jury:
            if x == self.jury[len(self.jury) - 1]:
                a += f"{x}"
                continue
            a += f"{x}, "
        return a

    def __str__(self):
        return f"Секция {self.id}, {self.name}, жюри в ней: {self.get_jury()}"
