class People:
    def __init__(self, id, name, l_name):
        self.id = id
        self.name = name
        self.last_name = l_name

    def __str__(self):
        return f"id = {self.id}, Имя {self.name}, Фамилия {self.last_name}"