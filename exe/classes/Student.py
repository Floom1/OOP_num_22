from .People import People

class Student(People):
    def __init__(self, id_, name, last_name):
        super().__init__(id_, name, last_name)
