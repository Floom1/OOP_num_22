from .People import People

class Jury(People):
    def __init__(self, id_, name, last_name):
        super().__init__(id_, name, last_name)
        self.students = []

    def __str__(self):
        return f"{self.name} {self.last_name}"
