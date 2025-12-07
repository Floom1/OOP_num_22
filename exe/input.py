from exe.classes.Jury import Jury
from exe.classes.Student import Student
from exe.classes.Section import Section

def get_data(file, clss):
    with open(file, "r", encoding="utf8") as f:
        data = f.readlines()
        it = []
        for line in data:
            res = line.strip().split()
            if res[0] == 'id':
                continue
            # it.append(res)
            if clss == Student:
                it.append(Student(res[0], res[1], res[2]))
            elif clss == Jury:
                it.append(Jury(res[0], res[1], res[2]))
            elif clss == Section:
                it.append(Section(res[0], res[1]))
        return it


def load_scores(conference, filename):
    with open(filename, "r", encoding="utf8") as f:
        for line in f:
            parts = line.strip().split()
            if parts[0] == 'id':
                continue
            section_id, jury_id, student_id, score = parts[1], parts[2], parts[3], int(parts[4])
            conference.add_score(jury_id, student_id, section_id, score)