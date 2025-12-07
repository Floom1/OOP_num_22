class Conference:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.juries = []
        self.sections = []
        self.scores = {}

    def add_student(self, st):
        self.students.append(st)

    def add_jury(self, jur):
        self.juries.append(jur)

    def add_section(self, sec):
        self.sections.append(sec)

    def find_student_by_id(self, id_):
        if self.students == []:
            return
        for x in self.students:
            if x.id == id_:
                return x

    def find_jury_by_id(self, id_):
        if self.juries == []:
            return
        for x in self.juries:
            if x.id == id_:
                return x

    def find_section_by_id(self, id_):
        if self.sections == []:
            return
        for x in self.sections:
            if x.id == id_:
                return x

    def add_score(self, j_id, st_id, sec_id, score):
        key = (st_id, sec_id)
        if key not in self.scores:
            self.scores[key] = []
        self.scores[key].append(score)

    def get_student_total_score_sec(self, st_id, sec_id):
        key = (st_id, sec_id)
        if key in self.scores:
            return sum(self.scores[key])
        return 0

    def get_student_total_score(self, st_id):
        summ = 0
        for x in self.scores.items():
            if str(st_id) == x[0][0]:
                summ += sum(x[1])
        return summ


    def __str__(self):
        a = f"Конференция {self.name}\n---------------------------\nСекции в ней:\n"
        for x in self.sections:
            a += f"Секция {x.id}, {x.name}, жюри в ней: {x.get_jury()}\n"
        a += "\n---------------------\nСтуденты в конференции:\n"
        for x in self.students:
            a += f"Ученик id = {x.id}, {x.name} {x.last_name}\n"
        for x in self.scores:
            a += f"Студент {self.find_student_by_id(x[0])}, секция {self.find_section_by_id(x[1]).name}, оценки: {self.scores[x]}\n"
        return a
